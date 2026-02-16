import jwt
from datetime import datetime
from app.keys import valid_key, expired_key

ALGORITHM = "RS256"

def generate_jwt(use_expired=False):
    key = expired_key if use_expired else valid_key

    payload = {
        "sub": "fakeUser",
        "iat": datetime.utcnow(),
        "exp": key.expiry
    }

    token = jwt.encode(
        payload,
        key.private_key,
        algorithm=ALGORITHM,
        headers={"kid": key.kid}
    )

    return token
