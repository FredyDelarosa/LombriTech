from sqlalchemy.orm import Session
from alertas.domain.ports.alerta_persistence_port import AlertaPersistencePort
from alertas.domain.entities.alerta import Alerta
from typing import List, Optional

class AlertaMySQLRepository(AlertaPersistencePort):
    def __init__(self, db: Session):
        self.db = db

    def crear_alerta(self, alerta: Alerta) -> Alerta:
        self.db.add(alerta)
        self.db.commit()
        self.db.refresh(alerta)
        return alerta

    def obtener_alertas(self) -> List[Alerta]:
        return self.db.query(Alerta).all()

    def obtener_alerta_por_id(self, alerta_id: int) -> Optional[Alerta]:
        return self.db.query(Alerta).filter(Alerta.id == alerta_id).first()

    def actualizar_alerta(self, alerta_id: int, nuevos_datos: dict) -> Optional[Alerta]:
        alerta = self.db.query(Alerta).filter(Alerta.id == alerta_id).first()
        if alerta:
            for clave, valor in nuevos_datos.items():
                setattr(alerta, clave, valor)
            self.db.commit()
            self.db.refresh(alerta)
        return alerta

    def eliminar_alerta(self, alerta_id: int) -> bool:
        alerta = self.db.query(Alerta).filter(Alerta.id == alerta_id).first()
        if alerta:
            self.db.delete(alerta)
            self.db.commit()
            return True
        return False
