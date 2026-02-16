from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta
import uuid

class Key:
    def __init__(self, private_key, kid, expiry):
        self.private_key = private_key
        self.public_key = private_key.public_key()
        self.kid = kid
        self.expiry = expiry

def generate_key(expiry_delta_hours):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    return Key(
        private_key=private_key,
        kid=str(uuid.uuid4()),
        expiry=datetime.utcnow() + timedelta(hours=expiry_delta_hours)
    )

# One valid key, one expired key
valid_key = generate_key(1)   # Expires in 1 hour
expired_key = generate_key(-1) # Already expired
