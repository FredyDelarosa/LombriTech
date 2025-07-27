from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal

class Turbidez(BaseModel):
    id: Optional[int]
    ntu: Optional[Decimal]
    fecha: Optional[datetime]
    composta_id: Optional[int]
    sst: Optional[Decimal]
