from typing import List, Dict
from samvidai.llm.prompts.qa import build_qa_prompt
from samvidai.llm.prompts.risk_analysis import build_risk_prompt


class LegalAgent:
    """
    High-level legal reasoning agent.
    """

    def __init__(self, provider):
        self.provider = provider

    def answer_question(
        self,
        question: str,
        contexts: List[Dict],
    ) -> str:
        """
        Answer a legal question using retrieved contract context.
        """
        prompt = build_qa_prompt(
            question=question,
            contexts=contexts,
        )
        return self.provider.generate(prompt)
    
    def analyze_clause_risk(self, clause_text: str) -> str:
        """
        Analyze risk for a single contract clause.
        """
        prompt = build_risk_prompt(clause_text)
        return self.provider.generate(prompt)
