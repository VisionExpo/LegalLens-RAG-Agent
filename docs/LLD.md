# Low-Level Design (LLD)

## Ingestion
- PDF → images (300 DPI)
- Preprocessing (deskew, denoise)

## Layout Processing
- LayoutLMv3 for region detection
- Bounding box metadata stored

## Retrieval
- Multimodal embeddings
- Vector DB indexing by region

## Reasoning
- Gemini 2.5 Pro on retrieved regions only

## Output
- Clause references
- Risk explanation
- Confidence indicators

