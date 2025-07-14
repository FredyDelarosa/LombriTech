from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from core.db.Database import get_db
from admin.infrastructure.service.mysql import UserSQLRepository
from admin.domain.entities.user import User
from utils.auth.token import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_user_repo(db: Session = Depends(get_db)) -> UserSQLRepository:
    return UserSQLRepository(db)


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    repo: UserSQLRepository = Depends(get_user_repo),
) -> User:
    claims = verify_token(token)
    if claims is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
        )

    user = repo.get_user_by_id(int(claims.get("sub")))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado",
        )
    return user
