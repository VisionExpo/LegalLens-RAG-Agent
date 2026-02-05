from pathlib import Path
import fitz  # PyMuPDF


class DigitalPDFTextExtractor:
    """
    Extracts per-page text from digitally generated PDFs.
    Used for govt contracts with an embedded text layer.
    """

    def __init__(self, pdf_path: Path):
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF not found: {pdf_path}")
        self.pdf_path = pdf_path

    def extract(self) -> list[dict]:
        doc = fitz.open(self.pdf_path)
        pages = []

        for page_index, page in enumerate(doc):
            text = page.get_text().strip()
            pages.append(
                {
                    "page_number": page_index + 1,
                    "text": text,
                }
            )

        return pages
