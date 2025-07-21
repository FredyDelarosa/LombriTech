from sqlalchemy.orm import Session
from admin.domain.entities.user import User
from admin.infrastructure.service.mysql import UserSQLRepository

def get_user_by_email(db: Session, email: str):
    repo = UserSQLRepository(db)
    return repo.get_user_by_email(email)

def create_user(db: Session, user: User):
    repo = UserSQLRepository(db)
    return repo.create_user(user)

def get_user_by_id(db: Session, user_id: int):
    repo = UserSQLRepository(db)
    return repo.get_user_by_id(user_id)

def update_user(db: Session, user: User):
    repo = UserSQLRepository(db)
    return repo.update_user(user)

def delete_user(db: Session, user: User):
    repo = UserSQLRepository(db)
    return repo.delete_user(user)