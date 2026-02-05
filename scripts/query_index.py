import sys
from samvidai.ingestion.config import DataSource, get_processed_path
from samvidai.retrieval.embedding import EmbeddingModel
from samvidai.retrieval.index import VectorIndex


def main():
    if len(sys.argv) < 3:
        raise SystemExit(
            "Usage: python scripts/query_index.py <data_source> <query text>"
        )

    source = DataSource(sys.argv[1])
    query = " ".join(sys.argv[2:])

    processed_dir = get_processed_path(source)
    index_dir = processed_dir / "index"

    index = VectorIndex.load(
        index_dir / "vectors.index",
        index_dir / "metadata.json",
    )

    embedder = EmbeddingModel()
    query_embedding = embedder.encode([query])

    results = index.search(query_embedding, top_k=5)

    print("\n--- TOP RESULTS ---\n")
    for r in results:
        print(f"[Score: {r['score']:.3f}] Page {r['page_number']}")
        print(r["text"][:300])
        print("-" * 40)


if __name__ == "__main__":
    main()
