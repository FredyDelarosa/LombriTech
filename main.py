from fastapi import FastAPI
from threading import Thread
from fastapi.middleware.cors import CORSMiddleware

from users.infrastructure.routes.user_routes import router as user_router
from compost_data.infrastructure.routes.data_router import router as compost_router
from compost_data.infrastructure.adapters.broker_listener import start_data_consumer

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

app.include_router(user_router)
app.include_router(compost_router)

def run_broker_consumer():
    start_data_consumer()
    
@app.on_event("startup")
def startup_event():
    print("Backend iniciado. Ejecutando consumidor de RabbitMQ...")
    Thread(target=run_broker_consumer, daemon=True).start()