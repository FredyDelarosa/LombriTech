from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from core.db.Database import get_db
from users.application.create_user import execute as create_uc
from users.application.login_user import execute as login_uc
from users.infrastructure.handlers.schemas import UserCreate

def register_controller(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    try:
        return create_uc(db, user_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

def login_controller(
    email: str,
    pwd: str,
    db: Session = Depends(get_db)
):
    try:
        return login_uc(db, email, pwd)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
