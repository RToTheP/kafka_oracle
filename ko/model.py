from typing import Optional

from pydantic import BaseModel


class Person(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str

class User(BaseModel):
    id: Optional[int] = None
    user_name: str