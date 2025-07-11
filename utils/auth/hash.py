from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

<<<<<<< HEAD
def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
=======
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
>>>>>>> f461c46 (feat: habilitar CRUD de usuarios para el admin con autenticación y autorización)
    return pwd_context.verify(plain_password, hashed_password)
