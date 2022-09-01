from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
import datetime


class Tara(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    img: str
    created_at: str = datetime.datetime.utcnow()
    updated_at: str = datetime.datetime.utcnow()
    tara_id: Optional[int] = Field(default=None, foreign_key="tara.id")


# class Tara(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     name: str
#     product: List["Product"] = Relationship(back_populates="tara")
#
#
# class Product(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     name: str
#     img: str
#     tara_id: Optional[int] = Field(foreign_key="tara.id", default=None)
#     tara: Optional[Tara] = Relationship(back_populates="products")
#     country_id: Optional[int] = Field(foreign_key="country.id", default=None)
#     created_at: str = datetime.datetime.utcnow()
#     updated_at: str = datetime.datetime.utcnow()
#
#
# class Country(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     name: str
