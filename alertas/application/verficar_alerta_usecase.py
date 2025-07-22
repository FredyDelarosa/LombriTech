from alertas.domain.ports.configuracion_port import ConfiguracionAlertaPort

def verificar_si_dispara_alerta(tipo_sensor: str, valor: float, composta_id: int, repo: ConfiguracionAlertaPort):
    config = repo.obtener_configuracion_sensor(tipo_sensor, composta_id)
    if not config:
        print(f"No hay configuración de alerta para {tipo_sensor} en composta {composta_id}")
        return

    if config.valor_minimo is not None and valor < config.valor_minimo:
        print(f"ALERTA: {tipo_sensor} = {valor} es menor que el mínimo permitido {config.valor_minimo}")
    elif config.valor_maximo is not None and valor > config.valor_maximo:
        print(f"ALERTA: {tipo_sensor} = {valor} es mayor que el máximo permitido {config.valor_maximo}")
    else:
        print(f"{tipo_sensor} = {valor} está dentro del rango permitido")