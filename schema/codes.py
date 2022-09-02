from pydantic import BaseModel
from datetime import datetime
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

class CodesAdd_and_Read(BaseModel):
    id: int
    code: str
    updated_at: datetime
    country_id: str
    product_id: str
    class Config:
        orm_mode = True

class CodesUpdate(BaseModel):
    id_codes: int
    codes: str
    country: str
    product: str
    class Config:
        orm_mode = True


