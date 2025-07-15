from users.domain.repositories.user_repository import get_user_by_email
from utils.auth.hash import verify_password
from utils.auth.token import create_access_token

def execute(db, correo: str, password: str) -> str:
    user = get_user_by_email(db, correo)
    if not user:
        raise ValueError("Usuario no encontrado")

    if not verify_password(password, user.password):
        raise ValueError("Contraseña incorrecta")

    token = create_access_token({"sub": user.correo})
    return token
