from typing import List, Dict


def build_qa_prompt(question: str, contexts: List[Dict]) -> str:
    context_text = "\n\n".join(
        f"[Page {c['page_number']}]\n{c['text']}"
        for c in contexts
    )

    return f"""
You are a legal contract analysis assistant.

Answer the question strictly using the provided contract excerpts.
If the answer is not present, say: "Not found in the provided document."

--- CONTRACT EXCERPTS ---
{context_text}

--- QUESTION ---
{question}

--- ANSWER ---
"""
