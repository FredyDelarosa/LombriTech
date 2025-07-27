from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from threading import Thread

from core.db.Database import Base, engine
from utils.middlewares.admin_only import AdminOnlyMiddleware

# Rutas existentes
from admin.infrastructure.routes.admin_user_routes import router as admin_user_routes
from admin.infrastructure.routes.auth_routes import router as auth_routes
from compost_data.infrastructure.routes.data_router import router as compost_router
from compost_analysis.infrastructure.routes.analysis_routes import router as analysis_router
from alertas.infrastructure.routes.alerta_routes import router as alerta_router
from alertas.infrastructure.routes.alerta_routes import router as notificaciones_router  # ✅ NUEVO
from compost_analysis.infrastructure.websockets.analysis_ws import router as ws_analysis
from compost_data.infrastructure.adapters.broker_listener import start_data_consumer
from reports.infrastructure.routes.report_route import router as report_router

from admin.infrastructure.startup import create_default_admin

# Crear las tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(title="LombriTech API")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Puedes cambiar esto si usas otro frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middlewares
app.add_middleware(AdminOnlyMiddleware, protected_prefixes=("/admin",))

# Rutas
app.include_router(admin_user_routes, prefix="/admin")
app.include_router(auth_routes, prefix="/auth")
app.include_router(compost_router)
app.include_router(analysis_router)
app.include_router(alerta_router)
app.include_router(notificaciones_router)  # ✅ NUEVA RUTA
app.include_router(ws_analysis)
app.include_router(report_router)

# Consumidor RabbitMQ en hilo separado
def run_broker_consumer():
    print("🌀 Iniciando consumidor de RabbitMQ...")
    Thread(target=start_data_consumer, daemon=True).start()

# Evento de inicio
@app.on_event("startup")
def startup_event():
    print("🚀 Backend iniciado.")
    create_default_admin()
    run_broker_consumer()
