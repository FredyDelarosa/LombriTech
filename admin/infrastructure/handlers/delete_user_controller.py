from fastapi import Request
from sqlalchemy.orm import Session
from admin.application.delete_user_uc import execute as delete_user_uc

async def delete_user_controller(
    request: Request,
    user_id: int,
    db: Session,
):
    current_user = request.state.user
    await delete_user_uc(db, user_id, current_user)
    return {"detail": "Usuario eliminado exitosamente"}