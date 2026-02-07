from fastapi import APIRouter, Depends, HTTPException

from api.schemas.rag import (
    AnalyzeContractRequest,
    AnalyzeContractResponse,
)
from api.schemas.risk import (
    AnalyzeRiskRequest,
    AnalyzeRiskResponse,
)
from api.deps import get_embedder, get_legal_agent, get_risk_engine

from samvidai.retrieval.index import VectorIndex


router = APIRouter()


# -------------------------
# Contract Q&A
# -------------------------
@router.post("/analyze/qa", response_model=AnalyzeContractResponse)
def analyze_qa(
    req: AnalyzeContractRequest,
    embedder=Depends(get_embedder),
    agent=Depends(get_legal_agent),
):
    index = VectorIndex.load_from_pdf(req.pdf_path)

    query_embedding = embedder.encode([req.question])
    clauses = index.search(query_embedding, top_k=req.top_k)

    answer = agent.answer_question(
        req.question,
        [c["text"] for c in clauses],
    )

    return AnalyzeContractResponse(
        answer=answer,
        retrieved_clauses=[
            {"clause_id": c["id"], "text": c["text"]}
            for c in clauses
        ],
    )


# -------------------------
# Risk Analysis
# -------------------------
@router.post("/analyze/risk", response_model=AnalyzeRiskResponse)
def analyze_risk(
    req: AnalyzeRiskRequest,
    embedder=Depends(get_embedder),
    agent=Depends(get_legal_agent),
    engines=Depends(get_risk_engine),
):
    classifier, scorer = engines

    index = VectorIndex.load_from_pdf(req.pdf_path)

    query_embedding = embedder.encode(
        ["termination penalty liability indemnity arbitration breach"]
    )
    clauses = index.search(query_embedding, top_k=10)

    risks = []
    for clause in clauses:
        analysis = agent.analyze_clause_risk(clause["text"])
        risks.append(
            {
                "clause_id": clause["id"],
                "risks": [analysis],
                "risk_score": classifier.classify(analysis),
            }
        )

    return AnalyzeRiskResponse(risks=risks)
