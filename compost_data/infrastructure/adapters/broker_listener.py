from core.broker.rabbitmq_client import get_connection, get_channel
from compost_data.application.process_data_usecase import procesar_mensaje
from compost_data.infrastructure.adapters.db_writer import DBSensorWriter
from alertas.infrastructure.adapters.config_mysql_adapter import ConfiguracionAlertaMySQLAdapter
from core.db.Database import SessionLocal
import json

def start_data_consumer():
    connection = get_connection()
    channel = get_channel(connection)

    sensor_repo = DBSensorWriter()
    exchange = "amq.topic"
    routing_keys = {
        "ph": "data.compost.pH",
        "humedad": "data.compost.humedad",
        "turbidez": "data.compost.turbidez",
        "conductividad": "data.compost.conductividad"
    }

    channel.exchange_declare(exchange=exchange, exchange_type='topic', durable=True)

    for tipo, routing_key in routing_keys.items():
        queue_name = routing_key

        channel.queue_declare(queue=queue_name, durable=True)
        channel.queue_bind(queue=queue_name, exchange=exchange, routing_key=routing_key)

        def make_callback(sensor_tipo):
            def callback(ch, method, properties, body):
                payload = json.loads(body.decode())
                print(f"[{sensor_tipo.upper()}] recibido:", payload)

                db = SessionLocal()
                try:
                    config_repo = ConfiguracionAlertaMySQLAdapter(db)
                    procesar_mensaje(sensor_tipo, payload, sensor_repo, config_repo)
                finally:
                    db.close()

            return callback

        channel.basic_consume(
            queue=queue_name,
            on_message_callback=make_callback(tipo),
            auto_ack=True
        )

    print("Escuchando múltiples colas de sensores...")
    channel.start_consuming()
