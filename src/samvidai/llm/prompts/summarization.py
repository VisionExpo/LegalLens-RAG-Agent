# src/samvidai/llm/prompts/summarization.py

SYSTEM_SUMMARY_PROMPT = """
You are a legal document summarizer.

Rules:
- Preserve legal meaning
- Avoid oversimplification
- Highlight obligations, rights, and liabilities
"""

def build_summary_prompt(context: list[str]) -> str:
    joined_context = "\n\n".join(context)
    return f"""
{SYSTEM_SUMMARY_PROMPT}

DOCUMENT CONTENT:
{joined_context}

SUMMARY:
"""
