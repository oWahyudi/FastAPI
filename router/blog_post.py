from fastapi import APIRouter, status,Response
from typing import Optional
from customenum import BlogType



router=APIRouter( prefix='/blog', tags=['Blog'])







@router.post('/new', summary="")
def create_blog():
    pass
    """
    This api call to create new blog record
    """
    

