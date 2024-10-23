from fastapi import APIRouter ,HTTPException ,Response, status
from app.schema import user_in , user_out
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db import get_db 
from typing import List
from app.tables import user
from app.utlity import Hash

router = APIRouter(prefix="/user",tags=["user"])

@router.post('/create',status_code = status.HTTP_201_CREATED)
def create_user(user_:user_in,db:Session=Depends(get_db)):
    user_.password= Hash(user_.password)
    result = user(**user_.dict())
    db.add(result)
    db.commit()
    db.refresh(result)
    return{"result":result}

@router.get("/get/{id}",status_code=status.HTTP_302_FOUND,response_model=user_out)
def get_user(id,db:Session=Depends(get_db)):
    result = db.query(user).filter(user.Id==id).first()
    if not result :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="These user is not found")
    return result

@router.get("/getall/",status_code=status.HTTP_302_FOUND,response_model=List[user_out])
def get_user(db:Session=Depends(get_db)):
    result = db.query(user).all()
    if not result :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="There is not user")
    print(result)
    return result


@router.delete("/delete/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id:int,db:Session=Depends(get_db)):
    result = db.query(user).filter(user.Id==id)
    if not result :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="These user is not found")
    result.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/update/{id}",status_code=status.HTTP_200_OK,response_model=user_out)
def update_user (id:int,user_:user_in,db:Session=Depends(get_db)):
    result = db.query(user).filter(user.Id==id)
    if not result :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="These user is not found")
    user_ = user_.dict()
    result.update(user_,synchronize_session=False)
    db.commit()
    return  result.first()
