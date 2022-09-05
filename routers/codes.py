from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import select, Session
from core.create_session import get_session, add_commit_refresh
from db.base import engine
from db.product import Product, Country
from db.code import Code
from schema.codes import CodesRead as Schema_Codes_Read
from schema.codes import CodesAdd as Schema_Codes_Add
from schema.codes import CodesAddOut as Schema_CodesAddOut
from schema.codes import CodesUpdate as Schema_Codes_Update
from schema.codes import CodesUpdateOut as Schema_CodesUpdateOut
from schema.codes import CodesRemove as Schema_CodesRemove

router = APIRouter()

@router.get('', name='Список кодов', status_code=200, response_model=List[Schema_Codes_Read])
async def get_codes(*, session: Session = Depends(get_session), limit: int = 100, skip: int = 0) -> list:
    codes = select(Code, Product, Country).join(Country, Country.id == Code.country_id).join(Product, Product.id == Code.product_id).limit(limit).offset(skip)
    return session.exec(codes).all()

@router.get('/{code}', name='Получить информацию по коду', status_code=200, response_model=Schema_Codes_Read)
async def get_cod(*, session: Session = Depends(get_session), code: str):
    codes = select(Code, Product, Country).join(Country, Country.id == Code.country_id).join(Product, Product.id == Code.product_id).where(Code.code == code)
    codes =  session.exec(codes).first()
    return Schema_Codes_Read(**codes.dict())

@router.post('/add', name='Добавление кодов', status_code=200, response_model=Schema_CodesAddOut, response_model_exclude={'updated_at', 'product_id', 'country_id'})
async def add_codes(*, session: Session = Depends(get_session), add: Schema_Codes_Add) -> Schema_CodesAddOut:
    country_db = select(Country).where(Country.name == add.country)
    country_db = session.exec(country_db).first()
    product_db = select(Product).where(Product.name == add.product)
    product_db = session.exec(product_db).first()

    code = Code(code=add.codes, country_id=country_db.id, product_id=product_db.id)
    add_commit_refresh(session, code)

    # Вставка данных в схему
    return Schema_CodesAddOut(id=code.id, code=code.code, created_at=code.created_at, country=country_db.name, product=product_db.name)

    # Schema_CodesA(**code.dict())

@router.put('{id_code}', name='Обновить код по ID', status_code=200, response_model=Schema_CodesUpdateOut)
async def update_codes(*, session: Session = Depends(get_session), update: Schema_Codes_Update) -> Schema_CodesUpdateOut:
    codes_db = select(Code).where(Code.id == update.id)
    codes_db = session.exec(codes_db).first()

    country_db = select(Country).where(Country.name == update.country)
    country_db = session.exec(country_db).first()

    product_db = select(Product).where(Product.name == update.product)
    product_db = session.exec(product_db).first()
    codes_db.code = update.code
    codes_db.country_id = country_db.id
    codes_db.product_id = product_db.id

    add_commit_refresh(session, codes_db)

    return Schema_CodesUpdateOut(id=codes_db.id, code=codes_db.code, updated_at=codes_db.updated_at, country=country_db.name, product=product_db.name)

@router.delete('{id_code}', name='Удалить код по ID', status_code=200, response_model=Schema_CodesRemove)
async def remove_code(*, session: Session = Depends(get_session), id_code: int):
    query = select(Code).where(Code.id == id_code)
    id_codes = session.exec(query).first()
    if not remove_code:
        raise HTTPException(status_code=404, detail="Код с данным ID не найдена")
    session.delete(id_codes)
    session.commit()
    return Schema_CodesRemove(output="Код с данным ID успешно удален")
