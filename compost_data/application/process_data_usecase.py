from compost_data.domain.ports.sensor_port import SensorPersistencePort

def procesar_mensaje(sensor_tipo: str, mensaje: dict, repo: SensorPersistencePort):
    dato = mensaje.get("valor")
    timestamp = mensaje.get("timestamp")
    composta_id = 1

    if dato is not None and timestamp:
        repo.guardar_valor_sensor(sensor_tipo, dato, timestamp, composta_id)
    else:
        print(f"Mensaje inválido para {sensor_tipo}: {mensaje}")
