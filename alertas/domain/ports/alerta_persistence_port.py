from abc import ABC, abstractmethod
from typing import List, Optional
from alertas.domain.entities.alerta import Alerta

class AlertaPersistencePort(ABC):
    @abstractmethod
    def crear_alerta(self, alerta: Alerta) -> Alerta:
        pass
    
    @abstractmethod
    def obtener_alertas(self) -> List[Alerta]:
        pass

    @abstractmethod
    def obtener_alerta_por_id(self, alerta_id: int) -> Optional[Alerta]:
        pass

    @abstractmethod
    def actualizar_alerta(self, alerta_id: int, nuevos_datos: dict) -> Optional[Alerta]:
        pass

    @abstractmethod
    def eliminar_alerta(self, alerta_id: int) -> bool:
        pass 
