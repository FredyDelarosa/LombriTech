from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Humedad(BaseModel):
    id: Optional[int]
    dato: Optional[int]
    fecha: Optional[datetime]
    composta_id: Optional[int]
