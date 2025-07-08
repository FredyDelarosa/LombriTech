from fastapi import APIRouter
from compost_data.infrastructure.handlers.data_controller import obtener_valores

router = APIRouter(prefix="/compost", tags=["Compost"])

@router.get("/valores/{tipo}")
def obtener_por_tipo(tipo: str):
    return obtener_valores(tipo)