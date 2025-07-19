from sqlalchemy.orm import Session
from users.domain.repositories.user_repository import create_user, get_user_by_email
from users.domain.entities.user import User
from utils.auth.hash import hash_password
from users.infrastructure.handlers.schemas import UserCreate
from utils.auth.auth import create_access_token 

def execute(db: Session, user_data: UserCreate):
    if get_user_by_email(db, user_data.correo):
        raise ValueError("Correo ya registrado")

    if user_data.password != user_data.password_confirm:
        raise ValueError("Las contraseñas no coinciden")

def execute(db, user_data):
    if get_user_by_email(db, user_data["correo"]):
        raise Exception("Correo ya registrado")

    user = User(
        nombre=user_data["nombre"],
        apellidos=user_data["apellidos"],
        rol=user_data["rol"],
        correo=user_data["correo"],
        password=hash_password(user_data["password"])
    )
    return create_user(db, user)
    user = User(
        nombre=user_data.nombre,
        apellidos=user_data.apellidos,
        rol=user_data.rol,
        correo=user_data.correo,
        password=hash_password(user_data.password)
    )

    create_user(db, user)

    token = create_access_token({"sub": user.correo})
    return token
