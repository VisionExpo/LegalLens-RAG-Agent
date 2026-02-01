from pdf2image import convert_from_path
from pathlib import Path

def pdf_to_images(pdf_path: str, output_dir: str) -> list[str]:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    images = convert_from_path(pdf_path, dpi=300)
    image_paths = []

    for i, img in enumerate(images):
        path = output_dir / f"page_{i+1}.png"
        img.save(path, "PNG")
        image_paths.append(str(path))

    return image_paths
