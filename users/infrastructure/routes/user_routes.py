from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.db.Database import get_db
from users.infrastructure.handlers.schemas import UserCreate, LoginRequest, Token
from users.infrastructure.handlers.create_user_controller import (
    register_controller,
    login_controller,
)

router = APIRouter(prefix="/users", tags=["Usuarios"])

@router.post("/register", response_model=UserCreate)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_controller(user, db)

@router.post("/login", response_model=Token)
def login(credentials: LoginRequest, db: Session = Depends(get_db)):
    return login_controller(credentials.email, credentials.password, db)
