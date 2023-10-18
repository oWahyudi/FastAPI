from pydantic import BaseModel
from typing import Optional



class BlogModel(BaseModel):
    title: str
    content: str
    nbcomment:int
    publish: Optional[bool]

