from sqlalchemy.orm import Session
from users.domain.repositories.user_repository import get_user_by_email
from utils.auth.hash import verify_password
from utils.auth.auth import create_access_token

def execute(db: Session, correo: str, password: str) -> str:
    user = get_user_by_email(db, correo)
    if not user:
        raise ValueError("Usuario no encontrado")

    if not verify_password(password, user.password):
        raise ValueError("Contraseña incorrecta")

    token = create_access_token(user_id=user.id)
    return token
