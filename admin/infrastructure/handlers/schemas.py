from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict


class UserCreate(BaseModel):
    nombre: str
    apellidos: str
    rol: str
    correo: EmailStr
    password: str
    password_confirm: str  
    usuario_telegram: str | None = None


class UserUpdate(BaseModel):
    nombre: str
    apellidos: str
    rol: str
    correo: EmailStr
    password: str
    password_confirm: str
    usuario_telegram: str | None = None

class UserPublic(BaseModel):
    id: int
    nombre: str
    apellidos: str
    rol: str
    correo: EmailStr
    created_at: datetime
    usuario_telegram: str | None = None
    model_config = ConfigDict(from_attributes=True)


class LoginRequest(BaseModel):
    correo: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"