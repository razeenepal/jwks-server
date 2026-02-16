from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_auth_valid():
    response = client.post("/auth")
    assert response.status_code == 200
    assert "token" in response.json()

def test_auth_expired():
    response = client.post("/auth?expired=true")
    assert response.status_code == 200
    assert "token" in response.json()
