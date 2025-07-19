from fastapi.testclient import TestClient
from run import app  # Asegúrate que 'run.py' contenga tu instancia FastAPI

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
