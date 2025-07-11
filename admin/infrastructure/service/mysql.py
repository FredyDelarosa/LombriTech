from sqlalchemy.orm import Session
from admin.domain.entities.user import User

class UserSQLRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_email(self, correo: str):
        return self.db.query(User).filter(User.correo == correo).first()

    def create_user(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_id(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def update_user(self, user: User):
        self.db.merge(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete_user(self, user: User):
        self.db.delete(user)
        self.db.commit()
