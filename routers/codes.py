from typing import List
from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from db.base import engine
from db.product import Product, Country
from db.code import Code
from schema.codes import CodesRead as Schema_Codes_Read
from schema.codes import CodesAdd as Schema_Codes_Add
from schema.codes import CodesUpdate as Schema_Codes_Update
from schema.codes import CodesAdd_and_Read as Schema_CodesAdd_and_Read


router = APIRouter()

@router.get('', name='Список кодов', status_code=200, response_model=List[Schema_Codes_Read])
async def get_codes(limit: int = 100, skip: int = 0) -> list:
    with Session(engine) as session:
        codes = select(Code, Product, Country).join(Country, Country.id == Code.country_id).join(Product, Product.id == Code.product_id).limit(limit).offset(skip)
        all_codes = session.exec(codes).all()
        return all_codes

@router.get('/{code}', name='Получить информацию по коду', status_code=200, response_model=Schema_Codes_Read)
async def get_cod(code: str):
    with Session(engine) as session:
        codes = select(Code, Product, Country).join(Country, Country.id == Code.country_id).join(Product, Product.id == Code.product_id).where(Code.code == code)
        all_codes = session.exec(codes).first()
        return all_codes

@router.post('/add', name='Добавление кодов', status_code=200)
async def add_codes(add: Schema_Codes_Add):
    with Session(engine) as session:
        country_db = select(Country).where(Country.name == add.country)
        country_db = session.exec(country_db).first()
        product_db = select(Product).where(Product.name == add.product)
        product_db = session.exec(product_db).first()


        code = Code(code=add.codes, country_id=country_db.id, product_id=product_db.id)
        session.add(code)
        session.commit()
        session.refresh(code)
        return code

@router.put('{id_code}', name='Обновить код по ID', status_code=200)
async def update_codes(id_codes: int, codes: str, country: str, product: str) -> list:
    with Session(engine) as session:
        codes_db = select(Code).where(Code.id == id_codes)
        codes_db = session.exec(codes_db).first()

        country_db = select(Country).where(Country.name == country)
        country_db = session.exec(country_db).first()

        product_db = select(Product).where(Product.name == product)
        product_db = session.exec(product_db).first()
        codes_db.code = codes
        codes_db.country_id = country_db.id
        codes_db.product_id = product_db.id

        session.add(codes_db)
        session.commit()
        session.refresh(codes_db)
        return codes_db

@router.delete('{id_code}', name='Удалить код по ID')
async def remove_code(id_code: int):
    with Session(engine) as session:
        query = select(Code).where(Code.id == id_code)
        id_codes = session.exec(query).first()
        if not remove_code:
            raise HTTPException(status_code=404, detail="Код с данным ID не найдена")

        session.delete(id_codes)
        session.commit()
        return {"ok": True}

