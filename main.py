from fastapi import FastAPI
from threading import Thread
from fastapi.middleware.cors import CORSMiddleware
from admin.infrastructure.startup import create_default_admin
from users.infrastructure.routes.user_routes import router as user_router
from compost_data.infrastructure.routes.data_router import router as compost_router
from compost_analysis.infrastructure.routes.analysis_routes import router as analysis_router
from compost_data.infrastructure.adapters.broker_listener import start_data_consumer
from sqlalchemy.orm import Session
from admin.domain.entities.user import User
from admin.infrastructure.service.mysql import UserSQLRepository
from core.db.Database import get_db
from utils.auth.hash import hash_password
from contextlib import contextmanager

from alertas.infrastructure.routes.alerta_routes import router as alerta_router

from utils.middlewares.admin_only import AdminOnlyMiddleware
from admin.infrastructure.routes.user_routes import router as user_routes
from admin.infrastructure.routes.auth_routes import router as auth_routes

from compost_analysis.infrastructure.websockets.analysis_ws import router as ws_analysis

from core.db.Database import Base, engine
from users.domain.entities import user
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(AdminOnlyMiddleware)
app.include_router(user_routes)
app.include_router(auth_routes)
app.include_router(user_router)
app.include_router(compost_router)
app.include_router(analysis_router)
app.include_router(alerta_router)
app.include_router(ws_analysis)

def run_broker_consumer():
    start_data_consumer()
    
@app.on_event("startup")
def startup_event():
    print("Backend iniciado. Ejecutando consumidor de RabbitMQ...")
    Thread(target=run_broker_consumer, daemon=True).start()


@contextmanager
def get_db_context():
    db = next(get_db())
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
def on_startup():

    if os.getenv("CREATE_ADMIN", "false").lower() == "true":
        create_default_admin()

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
