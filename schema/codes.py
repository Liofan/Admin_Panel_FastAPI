from typing import List, Optional, Dict, Union
from pydantic import BaseModel, Field
from .products import Product
from .country import Country


class Codes(BaseModel):
    id: int
    code: str

    class Config:
        orm_mode = True

class CodesRead(BaseModel):
    code: Codes
    product: Union[Product, List[Product]]
    country: Union[Country, List[Country]]

    class Config:
        orm_mode = True




