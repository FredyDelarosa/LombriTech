from fastapi import Request
from sqlalchemy.orm import Session
from admin.application.create_user_uc import execute as uc_create
from admin.infrastructure.handlers.schemas import UserCreate

async def create_user_controller(
    request: Request,
    db: Session,
    user_data: UserCreate,
):
    current_user = request.state.user  # viene del middleware
    return await uc_create(db, user_data, current_user)
