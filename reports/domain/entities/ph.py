from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal

class Ph(BaseModel):
    d: Optional[int]            # Nota: en tu tabla 'd' es PK
    dato: Optional[Decimal]
    fecha: Optional[datetime]
    composta_id: Optional[int]
