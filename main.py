from fastapi import FastAPI, HTTPException
import uvicorn

from core.auth import get_user_manager
from core.config import auth_backend
from db.base import engine
from routers import products, taras, codes, country, korob
import uuid

from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from db.user import User
from schema.users import UserRead, UserCreate, UserUpdate

app = FastAPI(title="API для воды", debug=True, version='0.1')



fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager,[auth_backend],)

app = FastAPI()

app.include_router( fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"])
app.include_router(fastapi_users.get_register_router(UserRead, UserCreate),prefix="/auth",tags=["auth"],)
app.include_router(fastapi_users.get_reset_password_router(),prefix="/auth",tags=["auth"],)
app.include_router(fastapi_users.get_verify_router(UserRead),prefix="/auth",tags=["auth"],)
app.include_router(fastapi_users.get_users_router(UserRead, UserUpdate),prefix="/users",tags=["users"],)

# Подлючение роутов
app.include_router(products.router, prefix="/products", tags=["Продукция"])
app.include_router(taras.router, prefix="/tara", tags=["Тара"])
app.include_router(country.router, prefix="/country", tags=["Страны"])
app.include_router(codes.router, prefix="/code", tags=["Потребительские Коды"])
app.include_router(korob.router, prefix="/korob", tags=["Ящики"])



@app.on_event("startup")
async def startup():
    engine.connect()

@app.on_event("shutdown")
async def shutdown():
    engine.dispose()

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, log_level="info")