from users.domain.entities.user import User
from users.domain.repositories.user_repository import create_user, get_user_by_email
from utils.auth.hash import hash_password

def execute(db, user_data):
    if get_user_by_email(db, user_data["email"]):
        raise Exception("Email already registered")
    user = User(
        nombre=user_data["nombre"],
        apellido_paterno=user_data["apellido_paterno"],
        apellido_materno=user_data["apellido_materno"],
        rol=user_data["rol"],
        email=user_data["email"],
        password=hash_password(user_data["password"])
    )
    return create_user(db, user)