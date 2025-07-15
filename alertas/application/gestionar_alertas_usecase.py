from alertas.domain.entities.alerta import Alerta
from alertas.domain.ports.alerta_persistence_port import AlertaPersistencePort
from typing import List, Optional

def crear_alerta_usecase(repo: AlertaPersistencePort, alerta: Alerta) -> Alerta:
    return repo.crear_alerta(alerta)

def listar_alertas_usecase(repo: AlertaPersistencePort) -> List[Alerta]:
    return repo.obtener_alertas()

def obtener_alerta_usecase(repo: AlertaPersistencePort, alerta_id: int) -> Optional[Alerta]:
    return repo.obtener_alerta_por_id(alerta_id)

def actualizar_alerta_usecase(repo: AlertaPersistencePort, alerta_id: int, nuevos_datos: dict) -> Optional[Alerta]:
    return repo.actualizar_alerta(alerta_id, nuevos_datos)

def eliminar_alerta_usecase(repo: AlertaPersistencePort, alerta_id: int) -> bool:
    return repo.eliminar_alerta(alerta_id)
