from typing import List, Optional, Dict
from pydantic import BaseModel, Field
from .products import Product
from .country import Country


class Codes(BaseModel):
    id: int
    code: str

    class Config:
        orm_mode = True

class CodesRead(Codes):
    code: str

    product: Product
    country: Country




