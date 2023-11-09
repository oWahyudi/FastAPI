from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime,timedelta
from jose import jwt

oauth2_schema= OAuth2PasswordBearer(tokenUrl='token')

#Create random string 32 bits using openssl
# >openssl rand -hex 32
SECRET_KEY='2cdeb1a09f869015440922d3d320ce6856d80b5836d0dbf822549033cb436cd4' 
#HMAC-SHA256
ALGORITHM='HS256'
ACCESS_TOKEN_EXPIRE_MINUTES =30

def create_access_token(data:dict, expires_delta: Optional[timedelta]=None):
    to_encode=data.copy()

    if expires_delta:
        expire=datetime.utcnow() + expires_delta
    else:
        expire=datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt


