from admin.infrastructure.service.mysql import UserSQLRepository
from utils.auth.hash import verify_password
from utils.auth.token import create_access_token
from fastapi import HTTPException, status

async def execute(db, login_data):
    repo = UserSQLRepository(db)
    user = repo.get_user_by_email(login_data.correo)
    if not user or not verify_password(login_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas")
    jwt = create_access_token({"sub": str(user.id), "rol": user.rol})
    return jwt
