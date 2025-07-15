from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.db.Database import get_db
from alertas.infrastructure.adapters.alerta_mysql_repository import AlertaMySQLRepository
from alertas.domain.entities.alerta import Alerta
from alertas.application.gestionar_alertas_usecase import (
    crear_alerta_usecase,
    listar_alertas_usecase,
    obtener_alerta_usecase,
    actualizar_alerta_usecase,
    eliminar_alerta_usecase
)
from alertas.infrastructure.schemas import AlertaCreate, AlertaUpdate, AlertaResponse
from typing import List

router = APIRouter(prefix="/alertas", tags=["Alertas"])

@router.post("/", response_model=AlertaResponse, status_code=status.HTTP_201_CREATED)
def crear_alerta(alerta_in: AlertaCreate, db: Session = Depends(get_db)):
    repo = AlertaMySQLRepository(db)
    alerta = Alerta(**alerta_in.dict())
    return crear_alerta_usecase(repo, alerta)

@router.get("/", response_model=List[AlertaResponse])
def obtener_alertas(db: Session = Depends(get_db)):
    repo = AlertaMySQLRepository(db)
    return listar_alertas_usecase(repo)

@router.get("/{alerta_id}", response_model=AlertaResponse)
def obtener_alerta(alerta_id: int, db: Session = Depends(get_db)):
    repo = AlertaMySQLRepository(db)
    alerta = obtener_alerta_usecase(repo, alerta_id)
    if not alerta:
        raise HTTPException(status_code=404, detail="Alerta no encontrada")
    return alerta

@router.put("/{alerta_id}", response_model=AlertaResponse)
def actualizar_alerta(alerta_id: int, alerta_in: AlertaUpdate, db: Session = Depends(get_db)):
    repo = AlertaMySQLRepository(db)
    alerta = actualizar_alerta_usecase(repo, alerta_id, alerta_in.dict(exclude_unset=True))
    if not alerta:
        raise HTTPException(status_code=404, detail="Alerta no encontrada")
    return alerta

@router.delete("/{alerta_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_alerta(alerta_id: int, db: Session = Depends(get_db)):
    repo = AlertaMySQLRepository(db)
    if not eliminar_alerta_usecase(repo, alerta_id):
        raise HTTPException(status_code=404, detail="Alerta no encontrada")
