from fastapi import APIRouter, Request, Depends, Security, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import List, Optional

from core.db.Databases import get_db
from admin.infrastructure.handlers.schemas import UserCreate, UserPublic, UserUpdate
from admin.infrastructure.handlers.create_user_controller import create_user_controller
from admin.infrastructure.handlers.list_users_controller import list_users_controller
from admin.infrastructure.handlers.update_user_controller import update_user_controller
from admin.infrastructure.handlers.delete_user_controller import delete_user_controller

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

router = APIRouter(
    prefix="/users",
    tags=["Usuarios"],
    dependencies=[Security(oauth2_scheme)]
)

@router.get("/", response_model=List[UserPublic])
async def listar_usuarios(
    request: Request,
    order_by: Optional[str] = "id",
    db: Session = Depends(get_db),
):
    return await list_users_controller(request, order_by, db)

@router.post("/", response_model=UserPublic, status_code=status.HTTP_201_CREATED)
async def crear_usuario(
    request: Request,
    user_data: UserCreate,
    db: Session = Depends(get_db),
):
    return await create_user_controller(request, db, user_data)

@router.put("/{user_id}", response_model=UserPublic)
async def actualizar_usuario(
    request: Request,
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db),
):
    return await update_user_controller(request, user_id, user_data, db)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_usuario(
    request: Request,
    user_id: int,
    db: Session = Depends(get_db),
):
    return await delete_user_controller(request, user_id, db)
