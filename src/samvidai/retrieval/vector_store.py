import faiss
import numpy as np

class VectorStore:
    def __init__(self, dim: int = 384):
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []

    def add(self, vectors, texts):
        self.index.add(np.array(vectors))
        self.texts.extend(texts)

    def search(self, query_vector, k=5):
        _, ids = self.index.search(query_vector, k)
        return [self.texts[i] for i in ids[0]]
