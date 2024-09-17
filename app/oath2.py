from jose import jwt, JWTError

from .schemas import TokenData
from .config import settings
from datetime import datetime, timedelta

from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
oath_scheme = OAuth2PasswordBearer(tokenUrl='login')




SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_time_expire_minutes

# creating access token  
def create_access_token(data: dict ): 
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

# verify access token 
def verify_access_token(token: str, credential_exception): 
    try : 
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    except: 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='unauthorized access')
    id: str = payload.get('user_id')

    if not id: 
        raise credential_exception

    token_data = TokenData(id=str(id))

    return token_data

# getting current user 
def get_current_user(token: str = Depends(oath_scheme)): 
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='unauthorized access')

    return verify_access_token(token, credential_exception)
