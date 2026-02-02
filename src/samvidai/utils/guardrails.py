from typing import List


MIN_CONTEXT_CHARS = 50
MIN_MATCHING_CLAUSES = 1


def has_sufficient_context(clauses: List[str]) -> bool:
    """
    Check whether retrieved context is sufficient
    to answer a question safely.
    """
    if not clauses or len(clauses) < MIN_MATCHING_CLAUSES:
        return False

    total_chars = sum(len(c) for c in clauses)
    return total_chars >= MIN_CONTEXT_CHARS
