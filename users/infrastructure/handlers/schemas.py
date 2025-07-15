from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    nombre: str
    apellidos: str
    rol: str
    correo: EmailStr
    password: str
    password_confirm: str  

class LoginRequest(BaseModel):
    correo: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
