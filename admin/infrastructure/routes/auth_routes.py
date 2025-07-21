from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from core.db.Database import get_db
from admin.infrastructure.handlers.schemas import LoginRequest, TokenResponse
from admin.infrastructure.handlers.login_user_controller import login_controller

router = APIRouter(tags=["Auth"])

@router.post("/login", response_model=TokenResponse, status_code=status.HTTP_200_OK)
async def login_endpoint(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    login_data = LoginRequest(
        correo=form_data.username,
        password=form_data.password
    )
    return await login_controller(login_data, db)
