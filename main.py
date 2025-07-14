from fastapi import FastAPI
<<<<<<< Updated upstream
<<<<<<< HEAD
from threading import Thread
from fastapi.middleware.cors import CORSMiddleware

=======
<<<<<<< HEAD
>>>>>>> 6-featureregister
from users.infrastructure.routes.user_routes import router as user_router
from compost_data.infrastructure.routes.data_router import router as compost_router
from compost_data.infrastructure.adapters.broker_listener import start_data_consumer

from core.db.Database import Base, engine
from users.domain.entities import user

app = FastAPI()
<<<<<<< HEAD

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(compost_router)

def run_broker_consumer():
    start_data_consumer()
    
@app.on_event("startup")
def startup_event():
    print("Backend iniciado. Ejecutando consumidor de RabbitMQ...")
    Thread(target=run_broker_consumer, daemon=True).start()
=======
app.include_router(user_router)
=======
from sqlalchemy.orm import Session
from admin.domain.entities.user import User
from admin.infrastructure.service.mysql import UserSQLRepository
from core.db.Databases import get_db
from utils.auth.hash import hash_password
from contextlib import contextmanager

=======
>>>>>>> Stashed changes
from utils.middlewares.admin_only import AdminOnlyMiddleware
from users.infrastructure.routes.user_routes import router as user_router
from admin.infrastructure.routes.user_routes import router as admin_user_router
from admin.infrastructure.routes.auth_routes import router as auth_routes
import os
from admin.infrastructure.startup import create_default_admin, get_db_context
from admin.infrastructure.service.mysql import UserSQLRepository
from admin.domain.entities.user import User
from utils.auth.hash import hash_password

app = FastAPI()

app.add_middleware(AdminOnlyMiddleware)

app.include_router(user_router)
app.include_router(admin_user_router)
app.include_router(auth_routes)

@app.on_event("startup")
def on_startup():
<<<<<<< Updated upstream
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
>>>>>>> 6-featureregister
=======
    if os.getenv("CREATE_ADMIN", "false").lower() == "true":
        create_default_admin()
>>>>>>> Stashed changes
