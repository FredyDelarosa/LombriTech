from fastapi import HTTPException, status
from admin.domain.entities.user import User
from admin.domain.repositories.user_repository import get_user_by_email, create_user
from utils.auth.hash import hash_password

async def execute(db, user_data, current_user=None):
    if current_user is None or current_user.rol.lower() != "administrador":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Solo administradores pueden crear usuarios"
        )

    if user_data.password != user_data.password_confirm:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Las contraseñas no coinciden"
        )

    if get_user_by_email(db, user_data.correo):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email ya registrado"
        )

    nuevo = User(
        rol=user_data.rol,
        nombre=user_data.nombre,
        apellidos=user_data.apellidos,
        correo=user_data.correo,
        password=hash_password(user_data.password)
    )
    return create_user(db, nuevo)
