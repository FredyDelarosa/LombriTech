import os
import pika
from dotenv import load_dotenv

load_dotenv()

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT", 5672))
RABBITMQ_USER = os.getenv("RABBITMQ_USER")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD")

def get_connection():
    try:
        credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
        parameters = pika.ConnectionParameters(
            host=RABBITMQ_HOST,
            port=RABBITMQ_PORT,
            credentials=credentials
        )
        connection = pika.BlockingConnection(parameters)
        print(f"✅ Conexión a RabbitMQ establecida en {RABBITMQ_HOST}:{RABBITMQ_PORT}")
        return connection
    except Exception as e:
        print(f"❌ Error al conectar a RabbitMQ: {e}")
        raise

def get_channel(connection: pika.BlockingConnection):
    try:
        channel = connection.channel()
        print("📡 Canal creado correctamente")
        return channel
    except Exception as e:
        print(f"❌ Error al crear canal: {e}")
        raise
