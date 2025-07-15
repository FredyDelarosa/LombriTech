# compost_data/domain/entities/composta.py
from sqlalchemy import Column, Integer, BigInteger
from core.db.Database import Base

class Composta(Base):
    __tablename__ = "composta"

    id = Column(BigInteger, primary_key=True)
