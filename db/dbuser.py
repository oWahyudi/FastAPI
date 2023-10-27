from sqlalchemy.orm.session import Session
from model.schema import UserBase
from db.dbschema import DbUser
from shared.hashlib import Hash
from fastapi import HTTPException,status

def create_user(db: Session, request: UserBase):
    newuser=DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(newuser)
    db.commit()
    db.refresh(newuser)
    return newuser

def get_all_user(db:Session):
    return db.query(DbUser).all()

def get_user(db:Session, id: int):
    user= db.query(DbUser).filter(DbUser.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with id {id} not found')
    return user

def update_user(db:Session, id:int, request:UserBase):
    user=db.query(DbUser).filter(DbUser.id==id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with id {id} not found')
    user.update({DbUser.username: request.username,
                 DbUser.email:request.email,
                 DbUser.password: Hash.bcrypt(request.password) })
    db.commit();
    return 'ok'

def delete_user(db:Session, id: int):
    user=db.query(DbUser).filter(DbUser.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with id {id} not found')
    db.delete(user)
    db.commit()
    return 'ok'
