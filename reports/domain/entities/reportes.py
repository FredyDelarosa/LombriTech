from pydantic import BaseModel
from typing import Optional
from datetime import date

class Reporte(BaseModel):
    id: Optional[int]
    fecha: Optional[date]
    alerta_id: Optional[int]
    composta_id: Optional[int]
    usuario_id: Optional[int]
