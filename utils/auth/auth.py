from datetime import datetime, timedelta
from authlib.jose import jwt, JoseError
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY") 
ALGORITHM = "HS256"

def create_access_token(data: dict, expires_delta: timedelta = timedelta(hours=1)) -> str:
    header = {"alg": ALGORITHM}
    payload = data.copy()
    expire = datetime.utcnow() + expires_delta
    payload["exp"] = int(expire.timestamp()) 
    return jwt.encode(header, payload, SECRET_KEY).decode("utf-8")

def verify_token(token: str):
    try:
        claims = jwt.decode(token, SECRET_KEY)
        claims.validate()
        return claims
    except JoseError:
        return None
