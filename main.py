from fastapi import FastAPI

from core.db.Database import Base, engine
from users.infrastructure.routes.user_routes import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="LombriTech API")
app.include_router(user_router)
