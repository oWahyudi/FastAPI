from fastapi import APIRouter, status,Response, Depends,Query,Body,Path
from typing import Optional,List
from shared.customenum import BlogType
from model.blog import BlogModel


router=APIRouter( prefix='/blog', tags=['Blog'])


def required_functionality():
    return {'message': 'Dummy output'}




@router.get('/all', summary="Retrieve all blogs")
def get_blogs(page=1,page_size:Optional[int]=None, req_parameter: dict=Depends(required_functionality)):
    """
    This api call simulate fething all blogs information
    """
    return {'message': f'all {page_size} blogs on page {page}', 'req': req_parameter}


@router.get('/type/{type}',summary="Retrieve blog by type id")
def get_blog_type(type: BlogType, req_parameter: dict=Depends(required_functionality)):
    """
    This api call to simulate querying blog by type id
    - **type** : mandatory path parameter
    """
    return {'message': f'BlogType {type}'}


@router.get('/{id}/comments/{comment_id}',tags=['Comment'],summary="Retrieve blog's comments")
def get_comments(id:int, comment_id:int, valid:bool=True, username:Optional[str]=None, req_parameter: dict=Depends(required_functionality)):
    """
    This api call to simulate querying all comments for the respective blog 
    - **id** : mandatory path parameter
    - **comment_id** : mandatory path parameter
    - **username** : optional query parameter
    """
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}


@router.get('/{id}', summary="Retrive blog by id")
def get_blog(id:int, response: Response, req_parameter: dict=Depends(required_functionality)):
    """
    This api call to fetching blog by id
    - **id** : mandatory path parameter
    """        
    if id > 5:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    else:
        response.status_code=status.HTTP_200_OK
        return {'message': f'Blog with id {id}'}
    







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

    



