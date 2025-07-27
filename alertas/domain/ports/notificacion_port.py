from abc import ABC, abstractmethod

class NotificacionTelegramPort(ABC):
    @abstractmethod
    def enviar_mensaje_usuario(self, username_telegram: str, mensaje: str) -> bool:
        pass
