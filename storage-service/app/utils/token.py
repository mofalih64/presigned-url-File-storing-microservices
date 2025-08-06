import jwt
from app.core.config import settings

def decode_token(token: str) -> dict:
    return jwt.decode(token, settings.presigned_secret_key, algorithms=["HS256"])
