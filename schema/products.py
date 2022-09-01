import datetime
from typing import List, Optional
from pydantic import BaseModel, Field

from schema.taras import TaraRead


class Product(BaseModel):
    id: int
    name: str
    img: str

class ProductRead(Product):
    id: int



