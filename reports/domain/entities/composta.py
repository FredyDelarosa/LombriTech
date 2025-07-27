from pydantic import BaseModel
from typing import Optional

class Composta(BaseModel):
    id: Optional[int]
    cantidad_composta_final: Optional[int]
    cant_lom_inicial: Optional[int]
    cant_lom_final: Optional[int]
    lote_id: Optional[int]
