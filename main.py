from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import contextmanager

from core.db.Database import Base, engine, get_db
from utils.middlewares.admin_only import AdminOnlyMiddleware
from admin.infrastructure.routes.admin_user_routes import router as admin_user_routes
from admin.infrastructure.routes.auth_routes import router as auth_routes
from admin.infrastructure.startup import create_default_admin

Base.metadata.create_all(bind=engine)

app = FastAPI(title="LombriTech API")

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],
)

app.add_middleware(AdminOnlyMiddleware, protected_prefixes=("/admin",))

app.include_router(admin_user_routes, prefix="/admin")
app.include_router(auth_routes, prefix="/auth")

@contextmanager
def get_db_context():
    db = next(get_db())
    try:
        yield db
    finally:
        db.close()

# Crear admin al iniciar
@app.on_event("startup")
def startup_event():
    create_default_admin()
