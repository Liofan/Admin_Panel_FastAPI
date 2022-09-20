from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from db.base import engine
from db.product import Product, Tara, Country

router = APIRouter()


@router.get('', name="Список продукции")
async def products_list(limit: int = 100, skip: int = 0):
    with Session(engine) as session:
        statement = select(Product, Tara, Country).join(Tara, Tara.id == Product.tara_id).join(Country, Country.id == Product.country_id).limit(limit).offset(skip)
        results = session.exec(statement).all()
        print(results)
        return results


@router.get('/tara/{volume}', name="Получить продукцию по таре")
async def get_products(volume: str):
    with Session(engine) as session:
        statement = select(Product, Tara).join(Tara).where(Tara.name == volume)
        results = session.exec(statement).all()
        return results



@router.post('/add', name="Добавить продукцию")
async def add_products(name: str, img: str, tara: str, country: str):
    with Session(engine) as session:
        country = Country(name=country)
        session.add(country)
        session.commit()
        session.refresh(country)

        tara = Tara(name=tara, country_id=country.id)
        session.add(tara)
        session.commit()
        session.refresh(tara)

        product = Product(name=name, img=img, tara_id=tara.id, country_id=country.id)
        session.add(product)
        session.commit()

        session.refresh(product)
        return product


@router.put('/{products_id}', name="Обновить продукцию по ID")
async def update_heroes(products_id: int, name: str, img: str, tara: str, country: str):
    with Session(engine) as session:
        query = select(Product).where(Product.id == products_id)
        products = session.exec(query).first()

        query = select(Tara).where(Tara.id == products_id)
        tara_db = session.exec(query).first()

        tara_db.name = tara

        session.add(tara_db)
        session.commit()
        session.refresh(tara_db)

        query = select(Country).where(Country.id == products_id)
        results_tara = session.exec(query)
        country_db = results_tara.one()

        country_db.name = country

        session.add(country_db)
        session.commit()
        session.refresh(country_db)

        products.name = name
        products.img = img
        products.tara_id = tara_db.id
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
