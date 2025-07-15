from sqlalchemy.orm import Session
from users.infrastructure.service.mysql import (
    mysql_get_user_by_email,
    mysql_create_user,
)
from users.domain.entities.user import User

def get_user_by_email(db: Session, email: str):
    return mysql_get_user_by_email(db, email)

def create_user(db: Session, user: User):
    return mysql_create_user(db, user)