from typing import List, Dict


class TextChunker:
    """
    Splits long text into overlapping semantic chunks.
    """

    def __init__(self, chunk_size: int = 800, overlap: int = 100):
        if overlap >= chunk_size:
            raise ValueError("overlap must be smaller than chunk_size")
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk_text(self, text: str) -> List[str]:
        chunks = []
        start = 0
        length = len(text)

        while start < length:
            end = start + self.chunk_size
            chunk = text[start:end].strip()
            if chunk:
                chunks.append(chunk)
            start = end - self.overlap

        return chunks

    def chunk_pages(
        self,
        pages: List[Dict],
        metadata: Dict,
    ) -> List[Dict]:
        all_chunks = []

        for page in pages:
            page_number = page["page_number"]
            text = page["text"]

            for idx, chunk in enumerate(self.chunk_text(text)):
                all_chunks.append(
                    {
                        "text": chunk,
                        "page_number": page_number,
                        "chunk_index": idx,
                        **metadata,
                    }
                )

        return all_chunks
