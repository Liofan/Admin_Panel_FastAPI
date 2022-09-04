from datetime import datetime
from typing import List

from pydantic import BaseModel
from .products import Product
from .country import Country


class Korob(BaseModel):
    id: int
    code: str
    country_id: int

    class Config:
        orm_mode = True

class Korob_codes(BaseModel):
    id: int
    codes: str
    korob_id: int
    created_at: str = datetime
    updated_at: str = datetime

    class Config:
        orm_mode = True

# class CodesAdd(BaseModel):
#     codes: str
#     country: str
#     product: str
#     class Config:
#         orm_mode = True
#
# class CodesUpdate(BaseModel):
#     id_codes: int
#     codes: str
#     country: str
#     product: str
#     class Config:
#         orm_mode = True
#

