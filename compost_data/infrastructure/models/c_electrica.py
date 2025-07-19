from sqlalchemy import Column, Integer, DECIMAL, ForeignKey, TIMESTAMP
from core.db.Database import Base

class ConductividadElectrica(Base):
    __tablename__ = "C_electrica"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ec = Column(DECIMAL(5, 2))
    tds = Column(DECIMAL(5, 2))
    fecha = Column(TIMESTAMP)
    composta_id = Column(Integer, ForeignKey("composta.id"))
