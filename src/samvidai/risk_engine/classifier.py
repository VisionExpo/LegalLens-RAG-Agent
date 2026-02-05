class RiskClassifier:
    """
    Classifies risk level from LLM risk analysis output.
    """

    LEVELS = ("HIGH", "MEDIUM", "LOW")

    def classify(self, analysis_text: str) -> str:
        text = analysis_text.upper()
        for level in self.LEVELS:
            if level in text:
                return level
        return "LOW"
