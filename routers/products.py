from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from db.base import engine
from db.product import Product, Tara, Country

router = APIRouter()


@router.get('', name="Список продукции")
async def products_list(limit: int = 100, skip: int = 0):
    with Session(engine) as session:
        statement = select(Product, Tara, Country).join(Tara, Tara.id == Product.tara_id).join(Country,
                                                                                               Country.id == Product.country_id).limit(
            limit).offset(skip)
        results = session.exec(statement).all()
        print(results)
        return results

# До думать
@router.get('/tara/{volume}', name="Получить продукцию по таре")
async def get_products(volume: str):
    with Session(engine) as session:
        statement = select(Product, Tara).join(Tara).where(Tara.name == volume)
        results = session.exec(statement).first()
        count = select(Country).where(Country.id == results.Tara.country_id)
        count = session.exec(count).first()
        return results, count


@router.post('/add', name="Добавить продукцию")
async def add_products(name: str, gtin: str, korob: int, img: str, tara: str, country: str):
    with Session(engine) as session:
        country_db = select(Country).where(Country.name == country)
        country_db = session.exec(country_db).first()
        if not country_db:
            raise HTTPException(status_code=404, detail="Данной страны нет в Базе Данных")
        tara_db = select(Tara).where(Tara.name == tara)
        tara_db = session.exec(tara_db).first()
        if not country_db:
            raise HTTPException(status_code=404, detail="Данной тары нет в Базе Данных")

        product = Product(name=name, gtin=gtin, korob=korob, img=img, tara_id=tara_db.id, country_id=country_db.id)
        session.add(product)
        session.commit()
        session.refresh(product)

        return product


@router.put('/{products_id}', name="Обновить продукцию по ID")
async def update_heroes(products_id: int, name: str, gtin: str, img: str, tara: str, country: str):
    with Session(engine) as session:
        query = select(Product).where(Product.id == products_id)
        products = session.exec(query).first()
        if not products:
            raise HTTPException(status_code=404, detail="Продукция с данным ID не найдена")
        country_db = select(Country).where(Country.name == country)
        country_db = session.exec(country_db).first()
        if not country_db:
            raise HTTPException(status_code=404, detail="Данной страны нет в Базе Данных")

        tara_db = select(Tara).where(Tara.name == tara)
        tara_db = session.exec(tara_db).first()
        if not country_db:
            raise HTTPException(status_code=404, detail="Данной тары нет в Базе Данных")

        products.name = name
        products.img = img
        products.gtin = gtin
        products.tara_id = tara_db.id
        products.country_id = country_db.id
        session.add(products)
        session.commit()
        session.refresh(products)

        return products


@router.delete('/{products_id}', name="Удалить продукцию по ID")
async def remove_products(tara_id: int):
    with Session(engine) as session:
        remove_products = session.get(Product, tara_id)
        if not remove_products:
            raise HTTPException(status_code=404, detail="Продукция с данным ID не найдена")
        session.delete(remove_products)
        session.commit()
        return {"ok": True}
