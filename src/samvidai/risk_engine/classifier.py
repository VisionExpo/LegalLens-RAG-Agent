from typing import List


# Keyword-based rules (can be extended or replaced later)
RISK_PATTERNS = {
    "termination": [
        "without notice",
        "immediate termination",
        "terminate at any time",
    ],
    "liability": [
        "unlimited liability",
        "indemnify",
        "hold harmless",
    ],
    "payment": [
        "late payment penalty",
        "interest on overdue",
        "non-refundable",
    ],
}


def classify_clause(text: str) -> List[str]:
    """
    Classify a clause into risk categories using rule-based matching.
    Returns list of detected risk categories.
    """
    text_lower = text.lower()
    detected = []

    for category, patterns in RISK_PATTERNS.items():
        for p in patterns:
            if p in text_lower:
                detected.append(category)
                break

    return detected
