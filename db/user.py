from typing import Optional, List
from sqlmodel import Field, SQLModel
import datetime



class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str = Field(primary_key=True, unique=True)
    hashed_password: str
    created_at: str = datetime.datetime.utcnow()
    updated_at: str = datetime.datetime.utcnow()




