import os
import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("KEY_BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

def enviar_mensaje_telegram(mensaje: str) -> bool:
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": mensaje
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("notificacion enviada")
        return True
    except requests.RequestException as e:
        print("ni para enviar un mensaje sirves cabron", e)
        return False
    except Exception as e:
        print("Error inesperado:", e)   