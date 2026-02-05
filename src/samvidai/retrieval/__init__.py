"""
Retrieval module for SamvidAI.

Provides semantic indexing and retrieval
for OpticalRAG-based contract analysis.
"""

from .embedding import EmbeddingModel
from .vector_store import VectorStore
from .retriever import Retriever

__all__ = [
    "EmbeddingModel",
    "VectorStore",
    "Retriever",
]
