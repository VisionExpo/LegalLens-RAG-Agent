from .embeddings import embed_texts

def retrieve(query: str, store):
    q_vec = embed_texts([query])
    return store.search(q_vec, k=5)
