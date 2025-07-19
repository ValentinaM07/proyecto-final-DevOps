from fastapi.testclient import TestClient
from run import app  # Asegúrate que tu app esté en run.py

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
