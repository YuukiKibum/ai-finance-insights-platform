from providers.base import BaseProvider
from config import OPENAI_API_KEY
import requests

class OpenAIProvider(BaseProvider):
    name = "openai"

    def generate(self, prompt: str) -> str:
        if not OPENAI_API_KEY:
            raise ValueError("Missing OPENAI_API_KEY")

        url = "https://api.openai.com/v1/chat/completions"

        payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code != 200:
            raise Exception(f"OpenAI error: {response.text}")

        data = response.json()
        return data["choices"][0]["message"]["content"]
