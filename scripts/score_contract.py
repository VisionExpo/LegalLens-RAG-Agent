import sys

from samvidai.ingestion.config import DataSource, get_processed_path
from samvidai.retrieval.embedding import EmbeddingModel
from samvidai.retrieval.index import VectorIndex
from samvidai.llm.providers.gemini_provider import GeminiProvider
from samvidai.llm.agents.legal_agent import LegalAgent
from samvidai.risk_engine.classifier import RiskClassifier
from samvidai.risk_engine.scorer import RiskScorer


def main():
    if len(sys.argv) < 2:
        raise SystemExit(
            "Usage: python scripts/score_contract.py <data_source>"
        )

    source = DataSource(sys.argv[1])

    processed_dir = get_processed_path(source)
    index_dir = processed_dir / "index"

    index = VectorIndex.load(
        index_dir / "vectors.index",
        index_dir / "metadata.json",
    )

    embedder = EmbeddingModel()
    query_embedding = embedder.encode(
        ["termination penalty liability indemnity arbitration breach"]
    )

    clauses = index.search(query_embedding, top_k=8)

    provider = GeminiProvider()
    agent = LegalAgent(provider)

    classifier = RiskClassifier()
    scorer = RiskScorer()

    clause_levels = []

    for clause in clauses:
        analysis = agent.analyze_clause_risk(clause["text"])
        level = classifier.classify(analysis)
        clause_levels.append(level)

    doc_risk = scorer.score(clause_levels)

    print("\n--- DOCUMENT RISK SUMMARY ---\n")
    print(f"Overall Risk Level: {doc_risk['risk_level']}")
    print(f"Risk Score: {doc_risk['risk_score']}/100")
    print(f"Clauses Analyzed: {doc_risk.get('clauses_analyzed', 0)}")


if __name__ == "__main__":
    main()
