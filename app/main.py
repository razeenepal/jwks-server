from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from datetime import datetime
from base64 import urlsafe_b64encode
from app.keys import valid_key
from app.jwt_utils import generate_jwt

app = FastAPI()

def rsa_to_jwk(key):
    public_numbers = key.public_key.public_numbers()
    n = urlsafe_b64encode(
        public_numbers.n.to_bytes((public_numbers.n.bit_length() + 7) // 8, 'big')
    ).rstrip(b"=").decode("utf-8")

    e = urlsafe_b64encode(
        public_numbers.e.to_bytes((public_numbers.e.bit_length() + 7) // 8, 'big')
    ).rstrip(b"=").decode("utf-8")

    return {
        "kty": "RSA",
        "use": "sig",
        "alg": "RS256",
        "kid": key.kid,
        "n": n,
        "e": e
    }

@app.get("/.well-known/jwks.json")
def jwks():
    if datetime.utcnow() > valid_key.expiry:
        return {"keys": []}

    return {"keys": [rsa_to_jwk(valid_key)]}

@app.post("/auth")
def auth(expired: bool = Query(False)):
    token = generate_jwt(use_expired=expired)
    return JSONResponse(content={"token": token})
