from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from core.db.Database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key = True, index = True)
    nombre = Column(String(25), nullable = False)
    apellido_paterno = Column(String(25), nullable = False)
    apellido_materno = Column(String(25), nullable = False)
    rol = Column(String(20), nullable = False)
    email = Column(String(50), unique = True, nullable = False)
    password = Column(String(100), nullable = False)
    created_at = Column(DateTime, default=datetime.utcnow)