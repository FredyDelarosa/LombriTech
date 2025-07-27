from admin.domain.entities.user import User

def execute(current_user: User):
    return {
        "Nombre": f"{current_user.nombre} {current_user.apellidos}",
        "Correo": current_user.correo,
        "Rol": current_user.rol,
        "userTelegram": current_user.usuario_telegram,
        "emailTelegram": current_user.correo
    }
