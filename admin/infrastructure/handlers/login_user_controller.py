from fastapi import Depends
from sqlalchemy.orm import Session
from core.db.Database import get_db
from admin.application.login_user import execute as login_uc
from admin.infrastructure.handlers.schemas import LoginRequest, TokenResponse

async def login_controller(
    login_data: LoginRequest,
    db: Session = Depends(get_db),
) -> TokenResponse:
    token = login_uc(db, login_data.correo, login_data.password)
    return TokenResponse(access_token=token)
