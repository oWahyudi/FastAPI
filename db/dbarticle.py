from sqlalchemy.orm.session import Session
from model.schema import ArticleBase
from db.dbschema import DbArticle
from shared.hashlib import Hash
from shared.customexception import StoryException
from fastapi import HTTPException,status


def create_article(db:Session, request: ArticleBase):
    if request.content.startswith('testcustomexception'):
        raise StoryException('Custom Exception triggered')
    newarticle=DbArticle(
        title = request.title,
        content = request.content,
        published = request.published,
        user_id=request.creator_id
    )
    db.add(newarticle)
    db.commit()
    db.refresh(newarticle)
    return newarticle

def get_article(db:Session, id: int):
    article=db.query(DbArticle).filter(DbArticle.id==id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Article with id {id} not found')
    return article


