from admin.domain.repositories.user_repository import get_user_by_email
from utils.auth.hash import verify_password
from utils.auth.token import create_access_token
from fastapi import HTTPException, status

def execute(db, correo: str, password: str) -> str:
    user = get_user_by_email(db, correo)
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas")
    token = create_access_token({"sub": str(user.id), "rol": user.rol})
    return token
