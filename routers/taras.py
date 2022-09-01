from typing import List

from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from db.base import engine
from db.product import Tara
from schema.taras import TaraRead

router = APIRouter()

@router.get('/tara', response_model=List[TaraRead], name="Получить все тары", tags=["Тара"])
async def get_tara():
    with Session(engine) as session:
        tara = select(Tara)
        result = session.exec(tara)
        tara_all = result.all()
    return tara_all

@router.get('/tara/{volume}', response_model=List[TaraRead] , name="Получить тару", tags=["Тара"])
async def get_tara(volume: str):
    with Session(engine) as session:
        tara = select(Tara).where(Tara.name == volume)
        result = session.exec(tara)
        tara_one = result.all()
    return tara_one

