from fastapi import FastAPI
from threading import Thread
from fastapi.middleware.cors import CORSMiddleware
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

from utils.middlewares.admin_only import AdminOnlyMiddleware
from admin.infrastructure.routes.user_routes import router as user_routes
from admin.infrastructure.routes.auth_routes import router as auth_routes

from core.db.Database import Base, engine
from users.domain.entities import user

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

def run_broker_consumer():
    start_data_consumer()
    
@app.on_event("startup")
def on_startup():
    if os.getenv("CREATE_ADMIN", "false").lower() == "true":
        create_default_admin()
