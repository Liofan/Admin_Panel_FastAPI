from .product import Product, Tara
from .code import Code
from .base import engine, SQLModel
from .user import User

SQLModel.metadata.create_all(engine)