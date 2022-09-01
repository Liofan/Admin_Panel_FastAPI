from starlette.config import Config

config = Config(".env")

DATABASE_URL = config("DATABASE_URl_PSQL", cast=str, default="")