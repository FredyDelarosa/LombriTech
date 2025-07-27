from fastapi import Request, HTTPException, status
from sqlalchemy.orm import Session
from admin.infrastructure.service.mysql import UserSQLRepository
from utils.auth.token import verify_token

async def get_current_user_controller(request: Request, db: Session):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token faltante o inválido")

    token = auth_header.split(" ")[1]
    claims = verify_token(token)
    if not claims:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido o expirado")

    user_id = int(claims.get("sub"))
    repo = UserSQLRepository(db)
    user = repo.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")

    return {
        "Nombre": f"{user.nombre} {user.apellidos}",
        "Correo": user.correo,
        "Rol": user.rol
    }
