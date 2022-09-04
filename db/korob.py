from sqlmodel import SQLModel, Field
import datetime
from typing import Optional
from .product import Product, Country


class Korob(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    group_code: str = Field(index=True)
    country_id: Optional[int] = Field(default=None, foreign_key="country.id")

class Korob_codes(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    codes: str
    korob_id: Optional[int] = Field(default=None, foreign_key="korob.id")
    created_at: str = datetime.datetime.utcnow()
    updated_at: str = datetime.datetime.utcnow()





