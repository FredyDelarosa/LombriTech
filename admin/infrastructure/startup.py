import os
from contextlib import contextmanager
from dotenv import load_dotenv

from core.db.Database import get_db
from admin.infrastructure.service.mysql import UserSQLRepository
from admin.domain.entities.user import User
from utils.auth.hash import hash_password

load_dotenv()

@contextmanager
def get_db_context():
    db = next(get_db())
    try:
        yield db
    finally:
        db.close()

def create_default_admin():
    if os.getenv("CREATE_ADMIN", "false").lower() != "true":
        print("⚠️ Creación de admin deshabilitada por variable de entorno")
        return

    admin_email = os.getenv("ADMIN_EMAIL")
    admin_password = os.getenv("ADMIN_PASSWORD")

    if not admin_email or not admin_password:
        print("⚠️ No se encontró email o contraseña para admin en variables de entorno")
        return

    with get_db_context() as db:
        repo = UserSQLRepository(db)
        existing_admin = repo.get_user_by_email(admin_email)

        if not existing_admin:
            new_admin = User(
                nombre="Admin",
                apellidos="Admin",
                rol="administrador",
                correo=admin_email,
                password=hash_password(admin_password)
            )
            repo.create_user(new_admin)
            print("Admin creado")
        else:
            print("ℹAdmin ya existe")
