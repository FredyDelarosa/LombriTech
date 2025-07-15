from sqlalchemy import Column, Integer, String, Float, ForeignKey
from core.db.Database import Base
from compost_data.domain.entities.composta import Composta

class Alerta(Base):
    __tablename__ = 'Alerta'
    
    id = Column(Integer, primary_key=True, index=True)
    valor_maximo = Column(Float, nullable=True)
    valor_minimo = Column(Float, nullable=True)
    tipo_sensor = Column(String(25), nullable=False)
    intervalo = Column(Integer, nullable=False)
    composta_id = Column(Integer, ForeignKey("composta.id"), nullable=False)
