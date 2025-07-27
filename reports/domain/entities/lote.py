from pydantic import BaseModel
from typing import Optional
from datetime import date

class Lote(BaseModel):
    id: Optional[int]
    fecha_inicio: Optional[date]
    fecha_final: Optional[date]
    descripcion: Optional[str]
