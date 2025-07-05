from fastapi import FastAPI
<<<<<<< HEAD
from users.infrastructure.routes.user_routes import router as user_router
from core.db.Database import Base, engine
from users.domain.entities import user

app = FastAPI()
app.include_router(user_router)
=======
from sqlalchemy.orm import Session
from admin.domain.entities.user import User
from admin.infrastructure.service.mysql import UserSQLRepository
from core.db.Databases import get_db
from utils.auth.hash import hash_password
from contextlib import contextmanager

from utils.middlewares.admin_only import AdminOnlyMiddleware
from admin.infrastructure.routes.user_routes import router as user_routes
from admin.infrastructure.routes.auth_routes import router as auth_routes

app = FastAPI()

app.add_middleware(AdminOnlyMiddleware)
app.include_router(user_routes)
app.include_router(auth_routes)


@contextmanager
def get_db_context():
    db = next(get_db())
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
def on_startup():
    with get_db_context() as db:
        repo = UserSQLRepository(db)

        admin_email = "admin@example.com"
        admin_user = repo.get_user_by_email(admin_email)

        if not admin_user:
            new_admin = User(
                nombre="Admin",
                apellidos="Admin",
                rol="administrador",  # en minúsculas
                correo=admin_email,
                password=hash_password("admin123")
            )
            repo.create_user(new_admin)
            print("Admin creado")
        else:
            print("Admin ya existe")
>>>>>>> f461c46 (feat: habilitar CRUD de usuarios para el admin con autenticación y autorización)
