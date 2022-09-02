from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from db.base import engine
from db.product import Product, Tara, Country
from core.create_session import get_session, add_commit_refresh

router = APIRouter()

@router.get('', name="Список продукции")
async def products_list(*, session: Session = Depends(get_session), limit: int = 100, skip: int = 0):
    statement = select(Product, Tara, Country).join(Tara, Tara.id == Product.tara_id).join(Country, Country.id == Product.country_id).limit(limit).offset(skip)
    return session.exec(statement).all()

@router.get('/tara/{volume}', name="Получить продукцию по таре")
async def get_products(*, session: Session = Depends(get_session), volume: str):
    statement = select(Product, Tara).join(Tara).where(Tara.name == volume)
    return session.exec(statement).all()

@router.post('/add', name="Добавить продукцию")
async def add_products(*, session: Session = Depends(get_session), name: str, img: str, tara: str, country: str):
    country = Country(name=country)
    add_commit_refresh(session, country)

    tara = Tara(name=tara, country_id=country.id)
    add_commit_refresh(session, tara)

    product = Product(name=name, img=img, tara_id=tara.id, country_id=country.id)
    add_commit_refresh(session, product)
    return product

@router.put('/{products_id}', name="Обновить продукцию по ID")
async def update_heroes(*, session: Session = Depends(get_session), products_id: int, name: str, img: str, tara: str, country: str):
    query = select(Product).where(Product.id == products_id)
    products = session.exec(query).first()

    query = select(Tara).where(Tara.id == products_id)
    tara_db = session.exec(query).first()

    tara_db.name = tara

    add_commit_refresh(session, tara_db)

    query = select(Country).where(Country.id == products_id)
    results_tara = session.exec(query)
    country_db = results_tara.one()

    country_db.name = country

    add_commit_refresh(session, country_db)

    products.name = name
    products.img = img
    products.tara_id = tara_db.id
    add_commit_refresh(session, products)
    return products

@router.delete('/{products_id}', name="Удалить продукцию по ID")
async def remove_products(*, session: Session = Depends(get_session), tara_id: int):
    remove_products = session.get(Product, tara_id)
    if not remove_products:
        raise HTTPException(status_code=404, detail="Продукция с данным ID не найдена")
    session.delete(remove_products)
    session.commit()
    return {"ok": True}
