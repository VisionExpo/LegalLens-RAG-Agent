# src/samvidai/llm/prompts/qa.py

SYSTEM_QA_PROMPT = """
You are SamvidAI, a legal contract analysis assistant.

Rules:
- Answer ONLY from the provided contract context.
- Do not hallucinate missing clauses.
- If the answer is not found, say "Not found in the provided contract."
- Prefer concise, legally precise language.
"""

def build_qa_prompt(question: str, context: list[str]) -> str:
    joined_context = "\n\n".join(context)
    return f"""
{SYSTEM_QA_PROMPT}

CONTRACT CONTEXT:
{joined_context}

QUESTION:
{question}

ANSWER:
"""
