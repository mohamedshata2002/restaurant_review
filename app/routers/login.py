from fastapi import HTTPException,status,APIRouter,Depends
from app.db import get_db
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from  app.schema import Token_response
from app.utlity import compare_pwd
from  app.tables import user
from app.othen import create_acess_token
router = APIRouter(tags=["authentication"])

@router.post("/login",response_model=Token_response)
def login(cred:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user_temp =  db.query(user).filter(user.email==cred.username).first()
    if not user_temp:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid credentials")

    if not compare_pwd(cred.password,user_temp.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid credentials")
    print("thanks ")
    access_token = create_acess_token(data={"user_id":user_temp.Id})
    token ={"token":access_token,"token_type":"bearer"}
    
    return token