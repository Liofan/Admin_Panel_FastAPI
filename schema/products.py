import datetime
from typing import List, Optional
from pydantic import BaseModel, Field

from .country import CountryRead
from .taras import TaraRead


class Product(BaseModel):
    id: int
    name: str
    img: str

    class Config:
        orm_mode = True

class ProductRead(Product):
    country: List[CountryRead] = []
    country: List[TaraRead] = []
