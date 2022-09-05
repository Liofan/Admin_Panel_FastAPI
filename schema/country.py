from typing import List, Optional
from pydantic import BaseModel, Field

class Country(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class CountryRead(Country):
    pass

class CountryAdd(BaseModel):
    name: str

class CountryRemove(BaseModel):
    output: str