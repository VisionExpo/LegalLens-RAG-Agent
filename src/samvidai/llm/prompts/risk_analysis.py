# src/samvidai/llm/prompts/risk_analysis.py

SYSTEM_RISK_PROMPT = """
You are a legal risk analysis engine.

Your task:
- Identify risky clauses
- Explain why they are risky
- Assign a risk level: LOW, MEDIUM, HIGH
- Be conservative and legally grounded
"""

def build_risk_prompt(clause_text: str) -> str:
    return f"""
{SYSTEM_RISK_PROMPT}

CLAUSE:
{clause_text}

OUTPUT FORMAT:
- Risk Level:
- Explanation:
"""
