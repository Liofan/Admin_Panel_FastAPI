import datetime
from typing import List, Optional
from pydantic import BaseModel, Field

from .country import Country
from .taras import Tara


class Product(BaseModel):
    id: int
    name: str
    img: str

    class Config:
        orm_mode = True

class ProductRead(Product):
    country: List[Country] = []
    country: List[Tara] = []
