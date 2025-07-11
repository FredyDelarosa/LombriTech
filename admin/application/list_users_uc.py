from admin.domain.entities.user import User

async def execute(db, order_by: str = "id"):
    valid_order_fields = {"id", "nombre", "email", "rol"}
    if order_by not in valid_order_fields:
        order_by = "id"

    query = db.query(User)
    if order_by == "id":
        query = query.order_by(User.id)
    elif order_by == "nombre":
        query = query.order_by(User.nombre)
    elif order_by == "email":
        query = query.order_by(User.correo)
    elif order_by == "rol":
        query = query.order_by(User.rol)

    return query.all()
