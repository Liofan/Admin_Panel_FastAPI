from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from db.base import engine
from db.product import Product, Tara


router = APIRouter()


@router.get('/products', name="Список продукции", tags=["Продукция"])
async def products_list(limit: int = 100, skip: int = 0):
    with Session(engine) as session:
        statement = select(Product, Tara).join(Tara).limit(limit).offset(skip)
        results = session.exec(statement).all()
        print(results)
        return results

@router.get('/products/{tara_id}', name="Получить продукцию по таре", tags=["Продукция"])
async def get_tara(tara: str):
    with Session(engine) as session:
        statement = select(Product, Tara).join(Tara).where(Tara.name == tara)
        results = session.exec(statement).all()
        return results

@router.post('/products', name="Добавить продукцию", tags=["Продукция"])
async def add_products(name: str, img: str, tara: str):
    with Session(engine) as session:
        prod_tara = Tara(name=tara)
        session.add(prod_tara)
        session.commit()
        session.refresh(prod_tara)
        prod = Product(name=name, img=img, tara_id=prod_tara.id)
        session.add(prod)
        session.commit()

        session.refresh(prod)
        print("prod:", prod)
        return prod

@router.put('/products/{products_id}',  name="Обновить продукцию по ID", tags=["Продукция"])
async def update_heroes(products_id: int, name: str, img: str, tara: str):
    with Session(engine) as session:
        #statement = select(Product, Tara).join(Tara).where(Tara.id == tara_id)
        statement = select(Product).where(Product.id == products_id)
        results = session.exec(statement)
        products = results.one()
        print("products:", products)

        statement = select(Tara).where(Tara.id == products_id)
        results_tara = session.exec(statement)
        tara_db = results_tara.one()

        tara_db.name = tara

        session.add(tara_db)
        session.commit()
        session.refresh(tara_db)

        products.name = name
        products.img = img
        products.tara_id = tara_db.id
        session.add(products)
        session.commit()
        session.refresh(products)
        return products

@router.delete('/products/{products_id}', name="Удалить продукцию по ID", tags=["Продукция"])
async def remove_products(tara_id: int):
    with Session(engine) as session:
        remove_products = session.get(Product, tara_id)
        if not remove_products:
            raise HTTPException(status_code=404, detail="Продукция с данным ID не найдена")
        remove_tara = session.get(Tara, tara_id)
        session.delete(remove_products)
        session.delete(remove_tara)
        session.commit()
        return {"ok": True}