from sentence_transformers import SentenceTransformer
from typing import List

class EmbeddingModel:
    """
    Wrapper around sentence-transformers for consistent embeddings
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.dim = self.model.get_sentence_embedding_dimension()

    def encode(self, texts: List[str]):
        return self.model.encode(texts, show_progress_bar=False)
