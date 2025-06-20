from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from core.db.Database import get_db
from users.infrastructure.handlers.create_user_controller import create_user_controller
from users.domain.repositories.user_repository import get_user_by_email
from utils.auth.hash import verify_password
from utils.auth.jwt import create_access_token

router = APIRouter()

@router.post("/register")
def register(user: dict, db: Session = Depends(get_db)):
    return create_user_controller(db, user)

@router.post("/login")
def login(form_data: dict, db: Session = Depends(get_db)):
    user = get_user_by_email(db, form_data["email"])
    if not user or not verify_password(form_data["password"], user.password):
        return {"error": "Invalid credentials"}
    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}