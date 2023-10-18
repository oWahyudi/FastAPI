from fastapi import APIRouter, status,Response,Query, Path,Body
from typing import Optional,List
from customenum import BlogType
from model.blog_model import BlogModel




router=APIRouter( prefix='/blog', tags=['Blog'])






@router.post('/new/{id}', summary="")
def create_blog(blog: BlogModel, id:int, version: int=1):
    """
    This api call to create new blog record
    """
    blog.title="testing"
    return {'id':id,
            'version':version,
            'data':blog}


@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog:BlogModel,id:int, 
                   comment_title:str=Query(None,description="Title of the comment", alias="commentTitle"),
                   content:str=Body('Body Parameter default value sample'),
                   content2:str=Body(..., min_length=10, max_length=20, regex='^[a-z\s]*$'),
                   v: Optional[List[str]]=Query(['1','2','3']),
                   comment_id:int=Path(gt=5, le=10)
                   
):
    return{
        'body': blog,
        'id':id,
        'comment_title': comment_title,
        'content': content,
        'content2': content2,
        'v':v,
        'comment_id':comment_id
    }

    

