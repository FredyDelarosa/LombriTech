from compost_data.domain.ports.sensor_port import SensorPersistencePort
from alertas.domain.ports.configuracion_port import ConfiguracionAlertaPort
from alertas.application.verficar_alerta_usecase import verificar_si_dispara_alerta
from utils.services.telegram_notifier import enviar_mensaje_telegram

def procesar_mensaje(sensor_tipo: str, mensaje: dict, repo: SensorPersistencePort, config_repo: ConfiguracionAlertaPort):
    timestamp = mensaje.get("timestamp")
    composta_id = 1
    
    if sensor_tipo == "turbidez":
        ntu = mensaje.get("ntu")
        sst = mensaje.get("sst")
        if ntu is not None and sst is not None and timestamp:
            repo.guardar_turbidez(ntu, sst, timestamp, composta_id)
        else:
            print(f"Datos incompletos de turbidez: {mensaje}")
        return

    if sensor_tipo == "conductividad":
        ec = mensaje.get("ec")
        tds = mensaje.get("tds")
        if ec is not None and tds is not None and timestamp:
            repo.guardar_conductividad_electrica(float(ec), float(tds), timestamp, composta_id)
        else:
            print(f"Mensaje inválido de conductividad: {mensaje}")
    else:
        valor = mensaje.get("valor")
        if valor is not None and timestamp:
            repo.guardar_valor_sensor(sensor_tipo, float(valor), timestamp, composta_id)
            verificar_si_dispara_alerta(sensor_tipo, float(valor), composta_id, config_repo)
        else:
            print(f"Mensaje inválido para {sensor_tipo}: {mensaje}")


    """if dato is not None and timestamp:
        repo.guardar_valor_sensor(sensor_tipo, dato, timestamp, composta_id)
        verificar_si_dispara_alerta(sensor_tipo, float(dato), composta_id, config_repo)
    else:
        print(f"aquí si lo hiciste bien {sensor_tipo}: {mensaje}")"""
