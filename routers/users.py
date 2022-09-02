from typing import List, Optional
from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select

from core.security import hash_password
from db.base import engine
from db.user import User
from schema.users import User as schema_user
from schema.users import UserIn as schema_user_add

router = APIRouter()

@router.get('', name='Список всех пользователй', status_code=200, response_model=List[schema_user])
async def get_all(limit: int = 100, skip: int = 0) -> list:
    with Session(engine) as session:
        all_user = select(User).limit(limit).offset(skip)
        all_user = session.exec(all_user).all()
        return all_user

@router.get('/{id}', name="Получить пользователя по ID", status_code=200)
async def get_by_id(id: int) -> Optional[User]:
    with Session(engine) as session:
        query = select(User).where(User.id == id)
        user = session.exec(query)
        return user

@router.post('/add', name='Добавление пользователя', status_code=200)
async def add_codes(add: schema_user_add):
    with Session(engine) as session:

        user = User(name=add.name, email=add.email, hashed_password=hash_password(add.password))
        session.add(user)
        session.commit()
        session.refresh(user)

        return user

#
# @router.put('{id_code}', name='Обновить код по ID', status_code=200)
# async def update_codes(id_codes: int, codes: str, country: str, product: str) -> list:
#     with Session(engine) as session:
#         codes_db = select(Code).where(Code.id == id_codes)
#         codes_db = session.exec(codes_db).first()
#
#         country_db = select(Country).where(Country.name == country)
#         country_db = session.exec(country_db).first()
#
#         product_db = select(Product).where(Product.name == product)
#         product_db = session.exec(product_db).first()
#         codes_db.code = codes
#         codes_db.country_id = country_db.id
#         codes_db.product_id = product_db.id
#
#         session.add(codes_db)
#         session.commit()
#         session.refresh(codes_db)
#         return codes_db
#
# @router.delete('{id_code}', name='Удалить код по ID')
# async def remove_code(id_code: int):
#     with Session(engine) as session:
#         query = select(Code).where(Code.id == id_code)
#         id_codes = session.exec(query).first()
#         if not remove_code:
#             raise HTTPException(status_code=404, detail="Код с данным ID не найдена")
#
#         session.delete(id_codes)
#         session.commit()
#         return {"ok": True}
#
