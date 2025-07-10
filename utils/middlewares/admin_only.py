from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from utils.auth.token import verify_token
from core.db.Databases import SessionLocal
from admin.infrastructure.service.mysql import UserSQLRepository


class AdminOnlyMiddleware(BaseHTTPMiddleware):
 
    def __init__(self, app, protected_prefixes: tuple[str, ...] | None = None):
        super().__init__(app)
        self.protected_prefixes = protected_prefixes or ("/users",)

    async def dispatch(self, request: Request, call_next):
        if (
            request.method not in {"GET", "OPTIONS", "HEAD"}
            and any(request.url.path.startswith(p) for p in self.protected_prefixes)
        ):
            auth_header = request.headers.get("Authorization")
            if not auth_header or not auth_header.startswith("Bearer "):
                return JSONResponse(status_code=401, content={"detail": "Falta token Bearer"})

            token = auth_header.split(" ", 1)[1]
            claims = verify_token(token)
            if claims is None:
                return JSONResponse(status_code=401, content={"detail": "Token inválido o expirado"})

            if claims.get("rol", "").lower() != "administrador":
                return JSONResponse(
                    status_code=403,
                    content={"detail": "Solo administradores pueden realizar esta acción"},
                )
            db = SessionLocal()
            try:
                repo = UserSQLRepository(db)
                request.state.user = repo.get_user_by_id(int(claims["sub"]))
            finally:
                db.close()

        return await call_next(request)
