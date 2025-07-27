from sqlalchemy.orm import Session
from alertas.domain.ports.notificacion_port import NotificacionTelegramPort
from admin.domain.repositories.user_repository import get_user_by_id
from fastapi import HTTPException, status

def enviar_notificacion_usuario_uc(
    db: Session,
    user_id: int,
    mensaje: str,
    notificador: NotificacionTelegramPort
):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    
    if not user.usuario_telegram:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario no tiene Telegram configurado"
        )

    enviado = notificador.enviar_mensaje_usuario(user.usuario_telegram, mensaje)
    if not enviado:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No se pudo enviar la notificación"
        )

    return {"message": "Notificación enviada correctamente"}
