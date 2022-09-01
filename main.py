from fastapi import FastAPI, HTTPException
import uvicorn
from db.base import engine
from routers import products, taras

app = FastAPI(title="Админ Панель", debug=True)

# Подлючение роутов
app.include_router(products.router)
app.include_router(taras.router)



@app.on_event("startup")
async def startup():
    engine.connect()

@app.on_event("shutdown")
async def shutdown():
    engine.dispose()

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, log_level="info")