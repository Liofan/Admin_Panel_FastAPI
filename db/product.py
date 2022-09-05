from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
import datetime


class Tara(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    country_id: Optional[int] = Field(default=None, foreign_key="country.id")

class Country(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    img: str
    created_at: str = datetime.datetime.utcnow()
    updated_at: str = datetime.datetime.utcnow()
    tara_id: Optional[int] = Field(default=None, foreign_key="tara.id")
    country_id: Optional[int] = Field(default=None, foreign_key="country.id")




