from fastapi import FastAPI
from users.infrastructure.routes.user_routes import router as user_router
from core.db.Database import Base, engine
from users.domain.entities import user

app = FastAPI()
app.include_router(user_router)