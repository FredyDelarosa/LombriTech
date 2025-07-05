from fastapi import Depends
from sqlalchemy.orm import Session
from core.db.Databases import get_db
from admin.application.login_user import execute as login_uc
from admin.infrastructure.handlers.schemas import LoginRequest, TokenResponse

async def login_controller(
    login_data: LoginRequest,
    db: Session = Depends(get_db),
) -> TokenResponse:
    token = await login_uc(db, login_data)
    return TokenResponse(access_token=token)
