from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from core.db.Database import get_db
from utils.auth.auth import verify_token
from users.domain.repositories.user_repository import get_user_by_email

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")

    user = get_user_by_email(db, payload["sub"])
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return user
