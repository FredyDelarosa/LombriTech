import os
import requests
from dotenv import load_dotenv
from alertas.domain.ports.notificacion_port import NotificacionTelegramPort

load_dotenv()

BOT_TOKEN = os.getenv("KEY_BOT_TOKEN")

class TelegramNotificacionAdapter(NotificacionTelegramPort):
    def enviar_mensaje_usuario(self, chat_id: int, mensaje: str) -> bool:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": mensaje
        }

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            print("✅ Notificación enviada")
            return True
        except requests.RequestException as e:
            print("❌ Error al enviar mensaje:", e)
            print("📦 Payload:", payload)
            if response is not None:
                print("🔁 Respuesta de Telegram:", response.text)
            return False
