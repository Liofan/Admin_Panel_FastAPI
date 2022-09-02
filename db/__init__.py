from .product import Product, Tara
from .code import Code
from .base import engine, SQLModel

SQLModel.metadata.create_all(engine)