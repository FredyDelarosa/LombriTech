from alertas.domain.ports.configuracion_port import ConfiguracionAlertaPort
from alertas.domain.entities.alerta import Alerta
from sqlalchemy.orm import Session
from typing import Optional

class ConfiguracionAlertaMySQLAdapter(ConfiguracionAlertaPort):
    def __init__(self, db: Session):
        self.db = db

    def obtener_configuracion_sensor(self, tipo_sensor: str, composta_id: int) -> Optional[Alerta]:
        return (
            self.db.query(Alerta)
            .filter(Alerta.tipo_sensor == tipo_sensor, Alerta.composta_id == composta_id)
            .first()
        )
