from typing import List
from sqlalchemy.exc import IntegrityError
import psycopg2
from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from db.base import engine
from db.product import Tara, Country
from schema.country import CountryRead as Schema_Country_Read
from schema.country import Country as Schema_Country

router = APIRouter()

@router.get('', response_model=List[Schema_Country_Read], name="Список стран")
async def get_taras() -> List[Schema_Country_Read]:
    """
    Вывод всех стран
    """
    with Session(engine) as session:
        country = select(Country)
        return session.exec(country).all()


@router.post('/add', response_model=Schema_Country, name='Добавление Страны')
async def add_country(country: str)  -> Schema_Country_Read:
    """
    Метод добавления страны
    Входящие параметры: Название страны
    Вывод: Добавленный обьект
    """
    with Session(engine) as session:
        try:
            country = Country(name = country)
            session.add(country)
            session.commit()
            session.refresh(country)
            return country
        except IntegrityError as e:
            raise HTTPException(status_code=404, detail='Данная Страна уже добавленна')

@router.delete('/{country_id}', response_model=Schema_Country,  name='Удаление страны по ID')
async def remove_country(country_id: int) -> Schema_Country_Read:
    """
    Метод удаления страны
    Входящие параметры: ID страны
    Вывод: Удаленный обьект
    """
    with Session(engine) as session:
        remove_country = session.get(Country, country_id)
        if not remove_country:
            raise HTTPException(status_code=404, detail='Cтраны с данным ID не найдена')
        session.delete(remove_country)
        session.commit()
        return {"ok": True}
