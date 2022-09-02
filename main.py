from fastapi import FastAPI, HTTPException
import uvicorn
from db.base import engine
from routers import products, taras, codes, country, users

app = FastAPI(title="API для воды", debug=True, version='0.1')

# Подлючение роутов
app.include_router(products.router, prefix="/products", tags=["Продукция"])
app.include_router(taras.router, prefix="/tara", tags=["Тара"])
app.include_router(country.router, prefix="/country", tags=["Страны"])
app.include_router(codes.router, prefix="/code", tags=["Потребительские Коды"])
app.include_router(users.router, prefix="/user", tags=["Пользователи"])


@app.on_event("startup")
async def startup():
    engine.connect()

@app.on_event("shutdown")
async def shutdown():
    engine.dispose()

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, log_level="info")