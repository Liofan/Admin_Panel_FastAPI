from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from core.create_session import get_session, add_commit_refresh
from db.base import engine
from db.product import Tara, Country
from schema.country import CountryRead as Schema_Country_Read
from schema.country import CountryAdd as Schema_CountryAdd
from schema.country import CountryRemove as Schema_CountryRemove

router = APIRouter()

@router.get('', response_model=List[Schema_Country_Read], name="Список стран")
async def get_country(*, session: Session = Depends(get_session)):
    """
    Вывод всех стран
    """
    country = select(Country)
    return session.exec(country).all()


@router.post('/add', name='Добавление Страны', response_model=Country)
async def add_country(*, session: Session = Depends(get_session), add: Schema_CountryAdd):
    """
    Метод добавления страны
    Входящие параметры: Название страны
    Вывод: Добавленный обьект
    """
    country = Country(name = add.name)
    add_commit_refresh(session, country)
    return Country(**country.dict())

@router.delete('/{country_id}', name='Удаление страны по ID', status_code=200, response_model=Schema_CountryRemove)
async def remove_country(*, session: Session = Depends(get_session), country_id: int):
    remove_country = session.get(Country, country_id)
    if not remove_country:
        raise HTTPException(status_code=404, detail='Cтраны с данным ID не найдена')
    session.delete(remove_country)
    session.commit()
    return Schema_CountryRemove(output="Страна с данным ID успешно удалена")
