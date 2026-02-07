from pydantic import BaseModel
from typing import List, Optional


class AnalyzeContractRequest(BaseModel):
    pdf_path: str
    question: str
    top_k: int = 5


class ClauseCitation(BaseModel):
    clause_id: str
    text: str


class AnalyzeContractResponse(BaseModel):
    answer: str
    retrieved_clauses: List[ClauseCitation]
