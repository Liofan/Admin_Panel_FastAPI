from pydantic import BaseModel
from .products import Product
from .country import Country


class Codes(BaseModel):
    id: int
    code: str

    class Config:
        orm_mode = True

class CodesRead(BaseModel):
    Code: Codes
    Product: Product
    Country: Country

    class Config:
        orm_mode = True

class CodesAdd(BaseModel):
    codes: str
    country: str
    product: str
    class Config:
        orm_mode = True

class CodesUpdate(BaseModel):
    id_codes: int
    codes: str
    country: str
    product: str
    class Config:
        orm_mode = True


