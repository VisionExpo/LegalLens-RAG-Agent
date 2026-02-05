import json
import sys
from pathlib import Path

from samvidai.ingestion.config import DataSource, get_processed_path
from samvidai.retrieval.embedding import EmbeddingModel
from samvidai.retrieval.index import VectorIndex


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python scripts/build_index.py <data_source>")

    source = DataSource(sys.argv[1])
    processed_dir = get_processed_path(source)
    chunk_dir = processed_dir / "chunks"

    chunk_files = list(chunk_dir.glob("*_chunks.json"))
    if not chunk_files:
        raise RuntimeError("No chunk files found. Run chunking first.")

    texts = []
    metadatas = []

    for file in chunk_files:
        with open(file, "r", encoding="utf-8") as f:
            chunks = json.load(f)

        for chunk in chunks:
            texts.append(chunk["text"])
            metadatas.append(chunk)

    embedder = EmbeddingModel()
    embeddings = embedder.encode(texts)

    index = VectorIndex(embedder.dim)
    index.add(embeddings, metadatas)

    index_dir = processed_dir / "index"
    index_dir.mkdir(parents=True, exist_ok=True)

    index.save(
        index_dir / "vectors.index",
        index_dir / "metadata.json",
    )

    print(f"[SUCCESS] Built index with {len(texts)} chunks")


if __name__ == "__main__":
    main()
