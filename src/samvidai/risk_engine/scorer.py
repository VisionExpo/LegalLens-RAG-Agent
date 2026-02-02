from domain.enums import RiskLevel


def score_risks(risks: list[str]) -> int:
    """
    Simple numeric risk score.
    """
    return len(risks)


def risk_level(score: int) -> RiskLevel:
    """
    Convert numeric score to RiskLevel enum.
    """
    if score >= 2:
        return RiskLevel.HIGH
    if score == 1:
        return RiskLevel.MEDIUM
    return RiskLevel.LOW
