import os
from datetime import datetime, timedelta
from authlib.jose import jwt, JoseError
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY: str = os.getenv("SECRET_KEY", "change-me")
ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_HOURS: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_HOURS", "1"))

def create_access_token(data: dict,
                        expires_delta: timedelta | None = None) -> str:
    if expires_delta is None:
        expires_delta = timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)

    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode["exp"] = int(expire.timestamp())

    header = {"alg": ALGORITHM}
    token = jwt.encode(header, to_encode, SECRET_KEY)
    return token

def verify_token(token: str) -> dict | None:
 
    try:
        claims = jwt.decode(token, SECRET_KEY)
        claims.validate()
        return claims
    except JoseError:
        return None
