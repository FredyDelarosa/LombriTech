from fastapi import Request
from sqlalchemy.orm import Session
from admin.application.create_user_uc import execute as uc_create
from admin.infrastructure.handlers.schemas import UserCreate

async def create_user_controller(
    request: Request = None,
    db: Session = None,
    user_data: UserCreate = None,
):
    current_user = getattr(request.state, "user", None) if request else None
    return await uc_create(db, user_data, current_user)
