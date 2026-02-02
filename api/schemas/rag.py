from pydantic import BaseModel, Field
from typing import List


class AnalyzeContractRequest(BaseModel):
    pdf_path: str = Field(..., description="Path to contract PDF")
    question: str = Field(..., description="Legal question to ask")


class AnalyzeContractResponse(BaseModel):
    answer: str
    retrieved_clauses: List[str]
