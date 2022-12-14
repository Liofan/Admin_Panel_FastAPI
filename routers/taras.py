from typing import List
from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from db.base import engine
from db.product import Tara, Country
from schema.taras import TaraRead

router = APIRouter()

@router.get('' , name="Список тар")
async def get_taras():
    with Session(engine) as session:
        tara = select(Tara, Country).join(Country ,Country.id == Tara.country_id)
        res = session.exec(tara).all()
        return res


@router.get('/{country}', name="Получить тару по Стране")
async def get_taras_by_country(country: str) -> List[TaraRead]:
    with Session(engine) as session:
        query = select(Tara, Country).join(Country).where(Country.name == country)
        res = session.exec(query).all()
        return res

@router.post('/add',  name='Добавление Тары')
async def add_taras(tara: str, country: str):
    with Session(engine) as session:
        query = select(Country).where(Country.name == country)
        country_db = session.exec(query).first()
        if not country_db:
            raise HTTPException(status_code=404, detail="Данной страны нет в Базе Данных")
        tara = Tara(name = tara, country_id = country_db.id)
        session.add(tara)
        session.commit()
        session.refresh(tara)
        return tara

@router.delete('/{tara_id}', name='Удаление тары по ID')
async def remove_tara(tara_id: int):
    with Session(engine) as session:
        remove_tara = session.get(Tara, tara_id)
        if not remove_tara:
            raise HTTPException(status_code=404, detail='Тара с данным ID не найдена')
        session.delete(remove_tara)
        session.commit()
        return {"ok": True}
