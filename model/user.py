from pydantic import BaseModel
from typing import Optional, List,Dict


class UserBase(BaseModel):
    username: str 
    email: str 
    password: str

class UserDisplay(BaseModel):
    username: str
    email: str
    class config():
        orm_mode=True
        


