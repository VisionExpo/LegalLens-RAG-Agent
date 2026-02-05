RISK_MAP = {
    "LOW": 20,
    "MEDIUM": 50,
    "HIGH": 80,
}


class RiskScorer:
    """
    Aggregates clause-level risks into document-level risk score.
    """

    def score(self, clause_levels: list[str]) -> dict:
        scores = [RISK_MAP[l] for l in clause_levels if l in RISK_MAP]

        if not scores:
            return {
                "risk_score": 0,
                "risk_level": "LOW",
                "note": "No risky clauses detected",
            }

        max_score = max(scores)
        avg_score = sum(scores) / len(scores)
        final_score = int(0.6 * max_score + 0.4 * avg_score)

        if final_score >= 70:
            level = "HIGH"
        elif final_score >= 40:
            level = "MEDIUM"
        else:
            level = "LOW"

        return {
            "risk_score": final_score,
            "risk_level": level,
            "clauses_analyzed": len(scores),
        }
