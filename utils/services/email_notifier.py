import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

def enviar_correo(asunto: str, mensaje: str) -> bool:
    msg = MIMEText(mensaje)
    msg["Subject"] = asunto
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        print("correo enviado con éxito")
        return True
    except smtplib.SMTPException as e:
        print("ni para enviar un correo sirves cabrón:", e)
        return False
    except Exception as e:
        print("Error inesperado:", e)
        return False
