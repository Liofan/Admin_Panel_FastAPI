from typing import List, Optional
from pydantic import BaseModel, Field

class Country(BaseModel):
    id: int


class CountryRead(Country):
    name: str