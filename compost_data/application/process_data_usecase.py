from compost_data.domain.ports.sensor_port import SensorPersistencePort
from alertas.domain.ports.configuracion_port import ConfiguracionAlertaPort
from alertas.application.verficar_alerta_usecase import verificar_si_dispara_alerta

def procesar_mensaje(sensor_tipo: str, mensaje: dict, repo: SensorPersistencePort, config_repo: ConfiguracionAlertaPort):
    dato = mensaje.get("valor")
    timestamp = mensaje.get("timestamp")
    composta_id = 1

    if dato is not None and timestamp:
        repo.guardar_valor_sensor(sensor_tipo, dato, timestamp, composta_id)
        verificar_si_dispara_alerta(sensor_tipo, float(dato), composta_id, config_repo)
    else:
        print(f"Mensaje inválido para {sensor_tipo}: {mensaje}")
