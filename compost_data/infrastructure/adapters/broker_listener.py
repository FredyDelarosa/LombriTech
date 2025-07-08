from core.broker.rabbitmq_client import get_connection, get_channel
from compost_data.application.process_data_usecase import procesar_mensaje
import json

def start_data_consumer():
    connection = get_connection()
    channel = get_channel(connection)
    
    exchange = "amq.topic"
    routing_key = "rasp/compost/datos"
    queue_name = "compost"
    
    channel.exchange_declare(exchange=exchange, exchange_type='topic', durable=True)
    channel.queue_declare(queue=queue_name, durable=True)
    channel.queue_bind(queue=queue_name, exchange=exchange, routing_key=routing_key)
    
    def callback(ch, method, properties, body):
        data = json.loads(body.decode())
        print("mensaje recibido:", data)
        procesar_mensaje(data)
        
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    print(f"Escuchando mensajes de '{routing_key}'...")
    channel.start_consuming()
