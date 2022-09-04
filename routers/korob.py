from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import select, Session
from core.create_session import get_session, add_commit_refresh
from db.base import engine
from db.product import Product, Country
from db.korob import Korob, Korob_codes
from schema.korob import Korob_codes as Schema_Korob_codes
router = APIRouter()

@router.get('', name='Список ящиков', status_code=200)
async def get_codes(*, session: Session = Depends(get_session), limit: int = 100, skip: int = 0) -> list:
    box = select(Korob, Korob_codes).limit(limit).offset(skip)
    return session.exec(box).all()

@router.get('/{code}', name='Получить информацию по коду', status_code=200)
async def get_cod(*, session: Session = Depends(get_session), code: str):
    korob = select(Korob).where(Korob.group_code == code)
    korob = session.exec(korob).first()
    korob_codes = select(Korob_codes).where(Korob_codes.korob_id == korob.id)
    korob_codes = session.exec(korob_codes).all()

    # statement = select(Korob, Korob_codes).join(Korob_codes).where(Korob_codes.korob_id == Korob.id)
    # korob = session.exec(statement).all()
    #z = Schema_Korob_codes(id=korob.id, codes=korob_codes, korob_id=korob.id)

    return korob, korob_codes



@router.post('/add', name='Добавление ящиков', status_code=200)
async def add_codes(*, session: Session = Depends(get_session), group_code: str, korob_codes: list, country: str):
    querye = select(Country).where(Country.name == country)
    country_id_id = session.exec(querye).first().id

    print(country_id_id)
    print(korob_codes)
    print(group_code)

    k = Korob(group_code=group_code, country_id=country_id_id)
    add_commit_refresh(session, k)

    for cod in korob_codes:
        print(cod)
        c = Korob_codes(codes=cod, korob_id=k.id)
        add_commit_refresh(session, c)

    #box = Box(group_code=group_code)

    return c

# @router.put('{id_code}', name='Обновить код по ID', status_code=200)
# async def update_codes(*, session: Session = Depends(get_session), id_codes: int, codes: str, country: str, product: str) -> list:
#     codes_db = select(Code).where(Code.id == id_codes)
#     codes_db = session.exec(codes_db).first()
#
#     country_db = select(Country).where(Country.name == country)
#     country_db = session.exec(country_db).first()
#
#     product_db = select(Product).where(Product.name == product)
#     product_db = session.exec(product_db).first()
#     codes_db.code = codes
#     codes_db.country_id = country_db.id
#     codes_db.product_id = product_db.id
#
#     add_commit_refresh(session, codes_db)
#
#     return codes_db
#
@router.delete('{id_code}', name='Удалить код по ID', status_code=200)
async def remove_code(*, session: Session = Depends(get_session), id_code: int):
    query = select(Korob).where(Korob.id == id_code)
    id_codes = session.exec(query).first()
    quer1y = select(Korob_codes).where(Korob_codes.korob_id == id_code)
    id_korob = session.exec(quer1y).all()
    if not remove_code:
        raise HTTPException(status_code=404, detail="Код с данным ID не найдена")
    session.delete(id_codes)
    session.delete(id_korob)
    session.commit()
    return {"ok": True}
