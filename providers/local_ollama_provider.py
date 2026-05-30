from providers.base import BaseProvider
from config import OLLAMA_MODEL
import requests

class LocalOllamaProvider(BaseProvider):
    name = "ollama"

    def generate(self, prompt: str) -> str:
        url = "http://localhost:11434/api/generate"

        payload = {
            "model": OLLAMA_MODEL,
            "prompt": prompt
        }

        response = requests.post(url, json=payload)

        if response.status_code != 200:
            raise Exception(f"Ollama error: {response.text}")

        data = response.json()
        return data.get("response", "")
