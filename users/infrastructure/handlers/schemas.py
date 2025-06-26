from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    rol: str
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
