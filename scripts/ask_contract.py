import sys

from samvidai.ingestion.config import DataSource, get_processed_path
from samvidai.retrieval.embedding import EmbeddingModel
from samvidai.retrieval.index import VectorIndex
from samvidai.llm.providers.gemini_provider import GeminiProvider
from samvidai.llm.agents.legal_agent import LegalAgent


def main():
    if len(sys.argv) < 3:
        raise SystemExit(
            "Usage: python scripts/ask_contract.py <data_source> <question>"
        )

    source = DataSource(sys.argv[1])
    question = " ".join(sys.argv[2:])

    processed_dir = get_processed_path(source)
    index_dir = processed_dir / "index"

    # Load vector index
    index = VectorIndex.load(
        index_dir / "vectors.index",
        index_dir / "metadata.json",
    )

    # Embed query
    embedder = EmbeddingModel()
    query_embedding = embedder.encode([question])

    # Retrieve context
    contexts = index.search(query_embedding, top_k=5)

    # LLM agent
    provider = GeminiProvider()
    agent = LegalAgent(provider)

    answer = agent.answer_question(question, contexts)

    print("\n--- ANSWER ---\n")
    print(answer)


if __name__ == "__main__":
    main()
