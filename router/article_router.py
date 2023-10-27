from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from db import dbarticle,database
from model.schema import ArticleBase,ArticleDisplay
from typing import List


router=APIRouter(prefix='/article',tags=['article'])

#create article
@router.post('/', response_model=ArticleDisplay)
def create_article(request:ArticleBase, db:Session=Depends(database.get_db)):
    return dbarticle.create_article(db,request)

#read article
@router.get('/{id}', response_model=ArticleDisplay)
def get_article(id:int, db:Session=Depends(database.get_db)):
    return dbarticle.get_article(db,id)


