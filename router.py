from fastapi import APIRouter
from providers.openai_provider import OpenAIProvider
from providers.local_ollama_provider import LocalOllamaProvider
from drift import detect_drift

router = APIRouter(prefix="/api")

# Provider order: primary → fallback
providers = [
    OpenAIProvider(),
    LocalOllamaProvider()
]

def run_with_fallback(prompt: str):
    """
    Try each provider in order.
    If one fails, automatically fall back to the next.
    """
    for provider in providers:
        try:
            response = provider.generate(prompt)
            if response:
                return {
                    "provider": provider.name,
                    "response": response
                }
        except Exception as e:
            print(f"Provider {provider.name} failed: {e}")

    return {"error": "All providers failed"}

@router.post("/finance-insights")
def finance_insights(data: dict):
    """
    Analyze financial data and return insights using LLMs.
    """
    prompt = f"""
    You are a financial analysis engine.
    Analyze the following financial data and provide insights:
    {data}
    """
    result = run_with_fallback(prompt)
    return result

@router.post("/risk-score")
def risk_score(data: dict):
    """
    Calculate a risk score (0–100) and detect drift.
    """
    drift = detect_drift(data)

    prompt = f"""
    You are a financial risk scoring engine.
    Based on this financial data, calculate a risk score (0-100)
    and explain the reasoning:
    {data}
    """

    result = run_with_fallback(prompt)
    result["drift_detected"] = drift
    return result
