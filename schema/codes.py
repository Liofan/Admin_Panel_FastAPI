from typing import List, Optional
from pydantic import BaseModel, Field

class Codes(BaseModel):
    id: int


class CodesRead(Codes):
    code: str