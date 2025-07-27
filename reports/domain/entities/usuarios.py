from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class Usuario(BaseModel):
    id: Optional[int]
    nombre: str
    apellidos: str
    rol: str
    correo: EmailStr
    contrasena_hash: str
    creado_en: Optional[datetime]
