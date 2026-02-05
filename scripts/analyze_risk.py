import sys

from samvidai.ingestion.config import DataSource, get_processed_path
from samvidai.retrieval.embedding import EmbeddingModel
from samvidai.retrieval.index import VectorIndex
from samvidai.llm.providers.gemini_provider import GeminiProvider
from samvidai.llm.agents.legal_agent import LegalAgent


def main():
    if len(sys.argv) < 2:
        raise SystemExit(
            "Usage: python scripts/analyze_risk.py <data_source>"
        )

    source = DataSource(sys.argv[1])

    processed_dir = get_processed_path(source)
    index_dir = processed_dir / "index"

    index = VectorIndex.load(
        index_dir / "vectors.index",
        index_dir / "metadata.json",
    )

    embedder = EmbeddingModel()

    # Broad legal-risk query
    query_embedding = embedder.encode(
        ["termination penalty liability indemnity arbitration breach"]
    )

    clauses = index.search(query_embedding, top_k=8)

    provider = GeminiProvider()
    agent = LegalAgent(provider)

    print("\n--- CLAUSE-LEVEL RISK ANALYSIS ---\n")

    for i, clause in enumerate(clauses, start=1):
        print(f"\n[Clause {i}] Page {clause['page_number']}")
        print(clause["text"][:500])
        print("\nRisk Analysis:")

        analysis = agent.analyze_clause_risk(clause["text"])
        print(analysis)
        print("-" * 60)


if __name__ == "__main__":
    main()
