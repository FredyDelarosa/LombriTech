from fastapi import Request
from sqlalchemy.orm import Session
from admin.application.list_users_uc import execute as list_users_uc

async def list_users_controller(
    request: Request,
    order_by: str,
    db: Session,
):
    # current_user = request.state.user  # disponible si lo necesitas
    return await list_users_uc(db, order_by)
