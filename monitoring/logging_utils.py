import time

def log_request(provider: str, prompt: str, response: str, latency_ms: float):
    print("\n--- REQUEST LOG ---")
    print(f"Provider: {provider}")
    print(f"Latency: {latency_ms:.2f} ms")
    print(f"Prompt: {prompt[:120]}...")
    print(f"Response: {response[:120]}...")
    print("-------------------\n")
