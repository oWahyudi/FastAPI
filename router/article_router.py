from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from db import dbarticle
from db.database import get_db
from model.schema import ArticleBase,ArticleDisplay
from typing import List
from auth.oauth2 import oauth2_schema


router=APIRouter(prefix='/article',tags=['article'])

#create article
@router.post('/', response_model=ArticleDisplay)
def create_article(request:ArticleBase, db:Session=Depends(get_db)):
    return dbarticle.create_article(db,request)

#read article
@router.get('/{id}', response_model=ArticleDisplay)
def get_article(id:int, db:Session=Depends(get_db), token: str=Depends(oauth2_schema)):
    return dbarticle.get_article(db,id)


