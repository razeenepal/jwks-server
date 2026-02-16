from fastapi.testclient import TestClient
from app.main import app
from datetime import datetime, timedelta
from app.keys import valid_key

client = TestClient(app)

def test_jwks_non_expired():
    # Only run if valid_key is not expired
    if datetime.utcnow() < valid_key.expiry:
        response = client.get("/.well-known/jwks.json")
        assert response.status_code == 200
        data = response.json()
        assert "keys" in data
        assert isinstance(data["keys"], list)
        assert len(data["keys"]) > 0

def test_jwks_expired():
    # Temporarily set key to expired
    original_expiry = valid_key.expiry
    valid_key.expiry = datetime.utcnow() - timedelta(hours=1)

    response = client.get("/.well-known/jwks.json")
    assert response.status_code == 200
    assert response.json() == {"keys": []}

    # Restore expiry
    valid_key.expiry = original_expiry
