from sqlalchemy import Column, Integer, DECIMAL, TIMESTAMP, ForeignKey
from core.db.Database import Base

class Turbidez(Base):
    __tablename__ = "Turbidez"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ntu = Column(DECIMAL(5, 2))
    sst = Column(DECIMAL(5, 2))
    fecha = Column(TIMESTAMP)
    composta_id = Column(Integer, ForeignKey("composta.id"))
