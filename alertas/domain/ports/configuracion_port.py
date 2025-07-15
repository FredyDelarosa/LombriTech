from abc import ABC, abstractmethod
from typing import Optional
from alertas.domain.entities.alerta import Alerta

class ConfiguracionAlertaPort(ABC):
    @abstractmethod
    def obtener_configuracion_sensor(self, tipo_sensor: str, composta_id: int) -> Optional[Alerta]:
        pass
