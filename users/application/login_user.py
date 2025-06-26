from sqlalchemy.orm import Session
from users.domain.repositories.user_repository import get_user_by_email
from utils.auth.hash import verify_password
from utils.auth.token import create_access_token

def execute(db: Session, email: str, password: str) -> dict:
    user = get_user_by_email(db, email)
    if user is None or not verify_password(password, user.password):
        raise ValueError("Credenciales incorrectas")

    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
