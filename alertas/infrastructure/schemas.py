from pydantic import BaseModel
from typing import Optional

class AlertaBase(BaseModel):
    valor_minimo: Optional[float]
    valor_maximo: Optional[float]
    tipo_sensor: str
    intervalo: int
    composta_id: int

class AlertaCreate(AlertaBase):
    pass

class AlertaUpdate(BaseModel):
    valor_minimo: Optional[float] = None
    valor_maximo: Optional[float] = None
    intervalo: Optional[int] = None

class AlertaResponse(AlertaBase):
    id: int

    class Config:
        orm_mode = True
