from pydantic import BaseModel
from typing import Optional, List, Dict


class Image(BaseModel):
    url: str
    alias: str

class BlogModel(BaseModel):
    title: str
    content: str
    nbcomment:int
    publish: Optional[bool]
    tags: List[str]=[]
    metadata: Dict[str,str]={'key1':'val1'}
    image: Optional[Image]=None



