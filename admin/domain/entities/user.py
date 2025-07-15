from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from core.db.Database import Base

class User(Base):
    __tablename__ = "usuarios"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    rol = Column(String(25), nullable=False)
    nombre = Column(String(25), nullable=False)
    apellidos = Column(String(50), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    password = Column("contrasena_hash", String, nullable=False)
    created_at = Column("creado_en", DateTime, default=datetime.utcnow)
