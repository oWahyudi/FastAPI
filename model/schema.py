from pydantic import BaseModel
from typing import Optional, List,Dict

#Article Inside User Display
class Article(BaseModel):
    title: str
    content:str
    published: bool
    class config():
        orm_mode=True

class UserBase(BaseModel):
    username: str 
    email: str 
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article]=[]
    class config():
        orm_mode=True


#User Inside Article Display
class User(BaseModel):
    id:int
    username:str
    class config():
        orm_mode=True


class ArticleBase(BaseModel):
    title : str
    content: str
    published: bool
    creator_id: int

class ArticleDisplay(BaseModel):
    title : str
    content: str
    published: bool
    user:User
    class config():
        orm_mode=True






        


