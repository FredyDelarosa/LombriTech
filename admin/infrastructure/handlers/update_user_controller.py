from fastapi import Request
from sqlalchemy.orm import Session
from admin.application.update_user_uc import execute as update_user_uc
from admin.infrastructure.handlers.schemas import UserUpdate

async def update_user_controller(
    request: Request,
    user_id: int,
    user_data: UserUpdate,
    db: Session,
):
    current_user = request.state.user
    return await update_user_uc(db, user_id, user_data, current_user)
