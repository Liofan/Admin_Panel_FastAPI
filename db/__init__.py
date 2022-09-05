from .product import Product, Tara
from .code import Code
from .base import engine, SQLModel
from .user import User
from .korob import Korob, Korob_codes

SQLModel.metadata.create_all(engine)