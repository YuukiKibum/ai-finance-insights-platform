from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

sample_data = {
    "transactions": [
        {"amount": 100},
        {"amount": 200},
        {"amount": 300}
    ]
}

def test_finance_insights():
    response = client.post("/api/finance-insights", json=sample_data)
    assert response.status_code == 200
    data = response.json()
    assert "provider" in data
    assert "response" in data

def test_risk_score():
    response = client.post("/api/risk-score", json=sample_data)
    assert response.status_code == 200
    data = response.json()
    assert "provider" in data
    assert "response" in data
    assert "drift_detected" in data
