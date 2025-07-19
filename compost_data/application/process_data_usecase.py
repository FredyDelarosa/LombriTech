from compost_data.domain.ports.sensor_port import SensorPersistencePort
from alertas.domain.ports.configuracion_port import ConfiguracionAlertaPort
from alertas.application.verficar_alerta_usecase import verificar_si_dispara_alerta
from utils.services.telegram_notifier import enviar_mensaje_telegram

def procesar_mensaje(sensor_tipo: str, mensaje: dict, repo: SensorPersistencePort, config_repo: ConfiguracionAlertaPort):
    dato = mensaje.get("valor")
    timestamp = mensaje.get("timestamp")
    composta_id = 1

    if dato is not None and timestamp:
        repo.guardar_valor_sensor(sensor_tipo, dato, timestamp, composta_id)
        verificar_si_dispara_alerta(sensor_tipo, float(dato), composta_id, config_repo)
        
        try:
            mensaje_alerta = (
                f"<b>ALERTA DE SENSOR</b>\n"
                f"tipo: {sensor_tipo.upper()}\n"
                f"valor: {dato}\n"
                f"fecha: {timestamp}\n"
                f"composta_id: {composta_id}\n"
            )
            if enviar_mensaje_telegram(mensaje_alerta):
                print("si se mandó :)")
            else:
                print("no se mandó :(")
        except Exception as e:
            print(f"algo estas haciendo mal wey: {e}")
    else:
        print(f"aquí si lo hiciste bien {sensor_tipo}: {mensaje}")
