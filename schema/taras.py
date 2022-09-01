from typing import List, Optional
from pydantic import BaseModel, Field

class Tara(BaseModel):
    id: int


class TaraRead(Tara):
    name: str