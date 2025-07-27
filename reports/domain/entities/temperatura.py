from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal

class Temperatura(BaseModel):
    id: Optional[int]
    dato: Optional[Decimal]
    fecha: Optional[datetime]
    composta_id: Optional[int]
