from fastapi import HTTPException
from users.application.create_user import execute

def create_user_controller(db, user_data):
    try:
        return execute(db, user_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))