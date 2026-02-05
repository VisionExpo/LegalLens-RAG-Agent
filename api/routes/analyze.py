from fastapi import APIRouter, Depends, HTTPException

from api.schemas.rag import RAGQuery
from api.schemas.risk import RiskResponse
from api.schemas.request_response import QAResponse
from api.deps import get_embedder, get_legal_agent, get_risk_engine

from samvidai.ingestion.config import DataSource, get_processed_path
from samvidai.retrieval.index import VectorIndex


router = APIRouter()


@router.post("/analyze/qa", response_model=QAResponse)
def analyze_qa(
    req: RAGQuery,
    embedder = Depends(get_embedder),
    agent = Depends(get_legal_agent),
):
    try:
        source = DataSource(req.data_source)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid data source")

    index_dir = get_processed_path(source) / "index"
    index = VectorIndex.load(
        index_dir / "vectors.index",
        index_dir / "metadata.json",
    )

    query_embedding = embedder.encode([req.question])
    contexts = index.search(query_embedding, top_k=req.top_k)

    answer = agent.answer_question(req.question, contexts)
    return QAResponse(answer=answer)


@router.post("/analyze/risk", response_model=RiskResponse)
def analyze_risk(
    req: RAGQuery,
    embedder = Depends(get_embedder),
    agent = Depends(get_legal_agent),
    engines = Depends(get_risk_engine),
):
    classifier, scorer = engines

    try:
        source = DataSource(req.data_source)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid data source")

    index_dir = get_processed_path(source) / "index"
    index = VectorIndex.load(
        index_dir / "vectors.index",
        index_dir / "metadata.json",
    )

    query_embedding = embedder.encode(
        ["termination penalty liability indemnity arbitration breach"]
    )
    clauses = index.search(query_embedding, top_k=req.top_k)

    levels = []
    for clause in clauses:
        analysis = agent.analyze_clause_risk(clause["text"])
        levels.append(classifier.classify(analysis))

    doc_risk = scorer.score(levels)

    return RiskResponse(
        risk_level=doc_risk["risk_level"],
        risk_score=doc_risk["risk_score"],
        clauses_analyzed=doc_risk.get("clauses_analyzed", 0),
    )
