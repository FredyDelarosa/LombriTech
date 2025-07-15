from sqlalchemy.orm import Session
from users.domain.entities.user import User

def mysql_get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def mysql_create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user