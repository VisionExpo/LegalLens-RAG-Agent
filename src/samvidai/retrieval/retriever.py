from typing import List, Dict
from samvidai.retrieval.embeddings import EmbeddingModel
from samvidai.retrieval.vector_store import VectorStore


class Retriever:
    """
    Semantic retriever with clause citation support
    """

    def __init__(self):
        self.embedder = EmbeddingModel()
        self.store = VectorStore(dim=self.embedder.dim)

    def index(self, clauses: List[Dict]):
        texts = [c["text"] for c in clauses]
        vectors = self.embedder.encode(texts)
        self.store.add(vectors, clauses)

    def retrieve(self, query: str, top_k: int = 5) -> List[Dict]:
        query_vec = self.embedder.encode([query])
        return self.store.search(query_vec, top_k=top_k)
