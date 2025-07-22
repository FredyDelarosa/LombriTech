from abc import ABC, abstractmethod

class SensorPersistencePort(ABC):
    @abstractmethod
    def guardar_valor_sensor(self, sensor: str, dato: float, timestamp: str, composta_id: int):
        pass
    
    @abstractmethod
    def guardar_conductividad_electrica(self, valor: float, timestamp: str, composta_id: int):
        pass
