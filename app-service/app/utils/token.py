import time
import jwt
from app.core.config import settings

def generate_token(data: dict) -> str:
    payload = {
        **data,
        "exp": int(time.time()) + settings.presigned_token_expiry,
    }
    return jwt.encode(payload, settings.presigned_secret_key, algorithm="HS256")

def decode_token(token: str) -> dict:
    return jwt.decode(token, settings.presigned_secret_key, algorithms=["HS256"])
