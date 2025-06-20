from sqlalchemy.orm import Session
from users.domain.entities.user import User

def mysql_get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def mysql_get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def mysql_get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def mysql_create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def mysql_delete_user(db: Session, user: User):
    db.delete(user)
    db.commit()

def mysql_update_user(db: Session, user: User, data: dict):
    for key, value in data.items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user