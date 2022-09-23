from typing import List, Optional
from pydantic import BaseModel, Field
from .country import Country

class Tara(BaseModel):
    id: int
    name: str
    country_id: int

class TaraRead(Tara):
    Tara: Tara
    Country: Country
    class Config:
        orm_mode = True