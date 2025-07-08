from pydantic import BaseModel
from datetime import datetime

class CompostRecord(BaseModel):
    timestamp: datetime
    ph: float
    turbidez: float
    humedad: float
    