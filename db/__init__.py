from .product import Product, Tara
from .base import engine, SQLModel

SQLModel.metadata.create_all(engine)

