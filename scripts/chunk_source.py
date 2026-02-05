import json
import sys
from pathlib import Path

from samvidai.chunking.chunker import TextChunker
from samvidai.ingestion.config import DataSource, get_processed_path


def main():
    if len(sys.argv) != 2:
        raise SystemExit(
            "Usage: python scripts/chunk_source.py <data_source>"
        )

    source = DataSource(sys.argv[1])
    processed_dir = get_processed_path(source)
    chunked_dir = processed_dir / "chunks"
    chunked_dir.mkdir(parents=True, exist_ok=True)

    chunker = TextChunker()

    for json_file in processed_dir.glob("*.json"):
        with open(json_file, "r", encoding="utf-8") as f:
            doc = json.load(f)

        chunks = chunker.chunk_pages(
            pages=doc["pages"],
            metadata={
                "source": doc["source"],
                "document_name": doc["document_name"],
            },
        )

        out_file = chunked_dir / f"{json_file.stem}_chunks.json"
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(chunks, f, indent=2, ensure_ascii=False)

        print(f"[CHUNKED] {json_file.name} → {out_file} ({len(chunks)} chunks)")


if __name__ == "__main__":
    main()
