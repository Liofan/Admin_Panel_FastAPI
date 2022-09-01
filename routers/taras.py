from typing import List

from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from db.base import engine
from db.product import Tara, Country
from schema.taras import TaraRead

router = APIRouter()

@router.get('', response_model=List[TaraRead], name="Список тар")
async def get_tara():
    with Session(engine) as session:
        tara = select(Tara)
        result = session.exec(tara)
        tara_all = result.all()
    return tara_all

@router.get('/{country}', name="Получить тару по Стране")
async def get_products(country: str):
    with Session(engine) as session:
        statement = select(Tara, Country).join(Country).where(Country.name == country)
        results = session.exec(statement).all()
        return results

