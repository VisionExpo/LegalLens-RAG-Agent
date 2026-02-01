def segment_layout(image_paths: list[str]) -> list[dict]:
    """
    Layout-aware segmentation placeholder.
    Each block simulates clause-level extraction.
    """
    blocks = []
    for img in image_paths:
        blocks.append({
            "source_image": img,
            "text": "Simulated clause text from layout model",
            "type": "clause"
        })
    return blocks
