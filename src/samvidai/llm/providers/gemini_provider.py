import os
import google.generativeai as genai
from samvidai.llm.providers.base import LLMProvider


class GeminiProvider(LLMProvider):
    """
    Gemini 2.5 Pro provider for legal reasoning
    """

    def __init__(self, model: str = "gemini-2.5-pro"):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("GEMINI_API_KEY not set")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model)

    def generate(self, prompt: str) -> str:
        response = self.model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.2,
                "top_p": 0.9,
            },
        )

        return response.text.strip()
