import os
from dotenv import load_dotenv
load_dotenv()
# API keys and model settings for providers

# Your OpenAI API key (replace with your real key)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Local Ollama model name (must match a model installed in Ollama)
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
