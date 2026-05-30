import time

metrics = {
    "provider_calls": {},
    "provider_failures": {},
    "latency": {}
}

def record_call(provider: str, latency_ms: float):
    metrics["provider_calls"][provider] = metrics["provider_calls"].get(provider, 0) + 1
    metrics["latency"][provider] = latency_ms

def record_failure(provider: str):
    metrics["provider_failures"][provider] = metrics["provider_failures"].get(provider, 0) + 1

def get_metrics():
    return metrics
