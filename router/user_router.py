from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from db import database,dbuser
from model.schema import UserBase,UserDisplay
from typing import List


router=APIRouter(prefix='/user',tags=['Users'])


# Create User
@router.post('/', response_model=UserDisplay)
def create_user(request:UserBase, db: Session=Depends(database.get_db)):
    return dbuser.create_user(db,request)


# Read User
@router.get('/', response_model=List[UserDisplay])
def get_all_users(db:Session=Depends(database.get_db)):
    return dbuser.get_all_user(db)

@router.get('{id}', response_model=UserDisplay)
def get_user(id: int, db: Session=Depends(database.get_db)):
    return dbuser.get_user(db,id)


# Update User
@router.post('{id}/update')
def update_user(id:int, request:UserBase, db: Session=Depends(database.get_db)):
    return dbuser.update_user(db,id,request)

# Delete User
@router.get('/delete/{id}')
def delete_user(id:int,db:Session=Depends(database.get_db)):
    return dbuser.delete_user(db,id)