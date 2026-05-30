# 🧠 AI Finance Insights Platform  
A modular, production‑style backend system that delivers financial insights, risk scoring, and intelligent LLM fallback routing using FastAPI, OpenAI, and local Ollama models.

This project is designed to demonstrate real‑world backend engineering skills:
- Clean architecture  
- Provider abstraction  
- Fallback logic  
- Monitoring & metrics  
- Drift detection  
- Automated tests  
- Example datasets  

---

## 🚀 Features

### 🔹 1. Finance Insights API
Send financial data and receive:
- Spending analysis  
- Behavioral insights  
- Category breakdowns  
- LLM‑generated explanations  

Endpoint:  
`POST /api/finance-insights`

---

### 🔹 2. Risk Scoring Engine
Calculates:
- Risk score (0–100)  
- Explanation from LLM  
- Drift detection flag  

Endpoint:  
`POST /api/risk-score`

---

### 🔹 3. Intelligent LLM Fallback System
Primary → OpenAI  
Fallback → Local Ollama  

If OpenAI fails (network, rate limit, outage), the system automatically switches to Ollama.

This is implemented in `run_with_fallback()`.

---

### 🔹 4. Monitoring & Metrics
Located in:
- `monitoring/logging_utils.py`
- `monitoring/metrics.py`

Tracks:
- Provider calls  
- Failures  
- Latency  
- Request logs  

---

### 🔹 5. Drift Detection
Simple placeholder in `drift.py`:
- Computes average transaction amount  
- Flags drift if above threshold  

Easy to upgrade to PSI, KS‑test, or ML‑based drift detection.

---

### 🔹 6. Automated Tests
Located in `tests/test_router.py`:
- Tests both endpoints  
- Validates response structure  
- Ensures drift flag exists  

Run tests with:

uv run pytest


---

## 🏗️ Project Structure

ai-finance-insights-platform/
│
├── main.py
├── router.py
├── config.py
├── drift.py
│
├── providers/
│   ├── base.py
│   ├── openai_provider.py
│   └── local_ollama_provider.py
│
├── monitoring/
│   ├── logging_utils.py
│   └── metrics.py
│
├── examples/
│   └── sample_transactions.json
│
└── tests/
└── test_router.py


---

## ⚙️ Installation & Setup

### 1. Create environment
uv venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Mac/Linux


### 2. Install dependencies
uv add fastapi uvicorn requests pytest dotenv


### 3. Run the server
uv run uvicorn main:app --reload


### 4. Open API docs  
http://127.0.0.1:8000/docs

---

## 🧪 Example Request

POST /api/finance-insights
{
"transactions": [
{"amount": 120},
{"amount": 450},
{"amount": 300}
]
}


---

## 🛠️ Tech Stack

- FastAPI — backend framework  
- OpenAI API — primary LLM  
- Ollama — local fallback LLM  
- uv — environment & dependency manager  
- Pytest — testing  
- Requests — HTTP client  

---

## 📌 Future Enhancements

- Replace drift placeholder with PSI or KS‑test  
- Add Prometheus metrics endpoint  
- Add Redis caching for repeated prompts  
- Add authentication (JWT)  
- Add Dockerfile for deployment  

---

## 📄 License
MIT License

---

## 👤 Author
Athira Jyothish Kumar — Telecom OSS/BSS engineer transitioning into Python/AI engineering.
