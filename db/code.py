from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
import datetime
from .product import Product, Country

class Code(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str = Field(index=True)
    created_at: str = datetime.datetime.utcnow()
    updated_at: str = datetime.datetime.utcnow()
    product_id: Optional[int] = Field(default=None, foreign_key="product.id")
    country_id: Optional[int] = Field(default=None, foreign_key="country.id")




