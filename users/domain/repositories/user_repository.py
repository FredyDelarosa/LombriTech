from sqlalchemy.orm import Session
from users.infrastructure.service.mysql import (
    mysql_get_user_by_email,
    mysql_get_user,
    mysql_get_users,
    mysql_create_user,
    mysql_delete_user,
    mysql_update_user,
)
from users.domain.entities.user import User

def get_user_by_email(db: Session, email: str):
    return mysql_get_user_by_email(db, email)

def get_user(db: Session, user_id: int):
    return mysql_get_user(db, user_id)

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return mysql_get_users(db, skip, limit)

def create_user(db: Session, user: User):
    return mysql_create_user(db, user)

def delete_user(db: Session, user: User):
    return mysql_delete_user(db, user)

def update_user(db: Session, user: User, data: dict):
    return mysql_update_user(db, user, data)