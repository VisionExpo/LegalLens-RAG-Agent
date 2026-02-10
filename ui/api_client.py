import os
import requests

API_BASE = os.getenv("SAMVID_API_URL", "http://localhost:8000")
MOCK_MODE = os.getenv("MOCK_MODE", "false").lower() == "true"

def analyze_contract(text: str):
    if MOCK_MODE:
        return {
            "risk_score": 0.72,
            "risk_level": "HIGH",
            "flags": [
                "Unilateral termination clause",
                "Missing indemnity cap",
                "Jurisdiction favors counterparty"
            ]
        }

    resp = requests.post(
        f"{API_BASE}/analyze",
        json={"contract_text": text},
        timeout=15
    )
    resp.raise_for_status()
    return resp.json()
