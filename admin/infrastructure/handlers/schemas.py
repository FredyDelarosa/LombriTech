from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict


class UserCreate(BaseModel):
    nombre: str
    apellidos: str
    rol: str
    correo: EmailStr
    password: str
    password_confirm: str  


class UserUpdate(BaseModel):
    nombre: str
    apellidos: str
    rol: str
    correo: EmailStr
    password: str
    password_confirm: str

class UserPublic(BaseModel):
    id: int
    nombre: str
    apellidos: str
    rol: str
    correo: EmailStr
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class LoginRequest(BaseModel):
    correo: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
