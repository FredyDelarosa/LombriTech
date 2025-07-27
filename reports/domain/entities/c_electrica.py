from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal

class CElectrica(BaseModel):
    id: Optional[int]
    ec: Optional[Decimal]
    fecha: Optional[datetime]
    composta_id: Optional[int]
    tds: Optional[Decimal]
