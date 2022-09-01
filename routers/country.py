from typing import List
from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from db.base import engine
from db.product import Tara, Country
from schema.country import CountryRead as Schema_Country_Read

router = APIRouter()

@router.get('', response_model=List[Schema_Country_Read], name="Список стран")
async def get_taras():
    """
    Вывод всех стран
    """
    with Session(engine) as session:
        country = select(Country)
        return session.exec(country).all()


@router.post('/add', name='Добавление Страны')
async def add_country(country: str):
    """
    Метод добавления страны
    Входящие параметры: Название страны
    Вывод: Добавленный обьект
    """
    with Session(engine) as session:
        country = Country(name = country)
        session.add(country)
        session.commit()
        session.refresh(country)
        return country

@router.delete('/{country_id}', name='Удаление страны по ID')
async def remove_country(country_id: int):
    with Session(engine) as session:
        remove_country = session.get(Country, country_id)
        if not remove_country:
            raise HTTPException(status_code=404, detail='Cтраны с данным ID не найдена')
        session.delete(remove_country)
        session.commit()
        return {"ok": True}
