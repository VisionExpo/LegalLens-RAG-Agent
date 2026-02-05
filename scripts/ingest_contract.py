from pathlib import Path
import json

from samvidai.layout.text_extractor import DigitalPDFTextExtractor

RAW_PDF = Path("data/govt_contracts/BARC_General_Conditions_of_Contract_GCC.pdf")
OUT_JSON = Path("data/processed/barc_gcc_pages.json")


def main():
    extractor = DigitalPDFTextExtractor(RAW_PDF)
    pages = extractor.extract()

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(pages, f, indent=2, ensure_ascii=False)

    print(f"[SUCCESS] Saved {len(pages)} pages to {OUT_JSON}")


if __name__ == "__main__":
    main()
