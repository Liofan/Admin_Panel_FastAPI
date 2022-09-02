from typing import List
from fastapi import APIRouter, HTTPException, Depends
from core.create_session import get_session, add_commit_refresh
from sqlmodel import Session, select
from db.base import engine
from db.product import Tara, Country
from schema.taras import TaraRead

router = APIRouter()

@router.get('', response_model=List[TaraRead], name="Список тар")
async def get_taras(*, session: Session = Depends(get_session)):
    tara = select(Tara)
    return session.exec(tara).all()

@router.get('/{country}', name="Получить тару по Стране")
async def get_taras_by_country(*, session: Session = Depends(get_session), country: str):
    query = select(Tara, Country).join(Country).where(Country.name == country)
    return session.exec(query).first()

@router.post('/add', name='Добавление Тары')
async def add_taras(*, session: Session = Depends(get_session), tara: str, country: str):
    query = select(Country).where(Country.name == country)
    country_db = session.exec(query).first()
    tara = Tara(name = tara, country_id = country_db.id)
    add_commit_refresh(session, tara)
    return tara

@router.delete('/{tara_id}', name='Удаление тары по ID')
async def remove_tara(*, session: Session = Depends(get_session), tara_id: int):
    remove_tara = session.get(Tara, tara_id)
    if not remove_tara:
        raise HTTPException(status_code=404, detail='Тара с данным ID не найдена')
    session.delete(remove_tara)
    session.commit()
    return {"ok": True}
