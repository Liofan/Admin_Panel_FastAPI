from starlette.config import Config
from fastapi_users.authentication import CookieTransport
from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy


config = Config(".env")

DATABASE_URL = config("DATABASE_URl_PSQL", cast=str, default="")

cookie_transport = CookieTransport(cookie_max_age=3600)
SECRET = "SECRET"
bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)