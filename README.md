# JWKS Server

A mini JWKS server implemented with FastAPI in Python.  
It serves public keys for JWT verification and issues JWTs with valid or expired keys for testing purposes.

## Features

- RSA 2048 key generation with unique `kid`  
- JWT issuance (RS256) with `kid` header  
- Key expiry handling  
- RESTful API endpoints:  
  - `/.well-known/jwks.json` → returns public keys  
  - `/auth` → returns signed JWT (`?expired=true` to get expired token)  
- Automated tests with pytest, coverage 100%

## Requirements

- Python 3.9+  
- Packages in `requirements.txt`

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
