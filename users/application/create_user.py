from users.domain.entities.user import User
from users.domain.repositories.user_repository import create_user, get_user_by_email
from utils.auth.hash import hash_password

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
