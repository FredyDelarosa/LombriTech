from fastapi import HTTPException, status
from admin.domain.repositories.user_repository import get_user_by_id, update_user

async def execute(db, user_id: int, user_data, current_user):
    if current_user.rol.lower() != "administrador":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Solo administradores pueden modificar usuarios")

    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")

    for key, value in user_data.dict(exclude_unset=True).items():
        setattr(user, key, value)

    return update_user(db, user)