from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from core.db.Database import get_db
from users.application.login_user import execute as login_uc

def login_controller(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    try:
        return login_uc(db, form_data.username, form_data.password)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
