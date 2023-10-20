from sqlalchemy.orm.session import Session
from model.user import UserBase
from db.dbschema import DbUser
from shared.hashlib import Hash

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
    return db.query(DbUser).filter(DbUser.id==id).first()

def update_user(db:Session, id:int, request:UserBase):
    user=db.query(DbUser).filter(DbUser.id==id)
    user.update({DbUser.username: request.username,
                 DbUser.email:request.email,
                 DbUser.password: Hash.bcrypt(request.password) })
    db.commit();
    return 'ok'

def delete_user(db:Session, id: int):
    user=db.query(DbUser).filter(DbUser.id==id).first()
    db.delete(user)
    db.commit()
    return 'ok'
