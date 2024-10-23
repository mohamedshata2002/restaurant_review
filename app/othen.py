import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime ,timedelta
from app.schema import Token_data
from fastapi import HTTPException,status,Depends
from fastapi.security.oauth2 import OAuth2PasswordBearer
from app.config import settings
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes
othen_scheme = OAuth2PasswordBearer(tokenUrl="login")
def create_acess_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encode = jwt.encode(to_encode,SECRET_KEY,ALGORITHM)
    return encode
    
def vertify_token(token,cred_exception):
    
    
    try:
        payload = jwt.decode(token,SECRET_KEY,[ALGORITHM])
        id :str = payload.get("user_id")
        if id is None:
            raise cred_exception
        token_data = Token_data(id=id)
    except InvalidTokenError:
        raise cred_exception
    return token_data
def get_current_user(token :str = Depends(othen_scheme)):
    cred_exp = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"})
    return vertify_token(token,cred_exp)