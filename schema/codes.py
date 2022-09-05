import datetime
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

class CodesAddOut(BaseModel):
    id: int
    code: str
    created_at: datetime.datetime
    country: str
    product: str
    class Config:
        orm_mode = True

class CodesUpdate(BaseModel):
    id: int
    code: str
    country: str
    product: str

    class Config:
        orm_mode = True

class CodesUpdateOut(BaseModel):
    id: int
    code: str
    country: str
    product: str
    updated_at: datetime.datetime

    class Config:
        orm_mode = True

class CodesRemove(BaseModel):
    output: str