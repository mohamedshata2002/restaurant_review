from fastapi import APIRouter ,HTTPException ,Response, status
from app.schema import review_in , review_out
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db import get_db 
from typing import List
from app.tables import Review ,restaurant
from app.othen import get_current_user
router = APIRouter(prefix="/review",tags=["review"])

@router.post('/create',status_code = status.HTTP_201_CREATED)
def create_review(resv:review_in,db:Session=Depends(get_db),userid:int=Depends(get_current_user)):
    id = resv.at_restaurant
    print(id)
    res = db.query(restaurant).filter(restaurant.Id==id).first()
    if not res:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="These restuarant is not found")
    resv.user_id = userid.id
    result = Review(**resv.dict())
    db.add(result)
    db.commit()
    db.refresh(result)
    return{"result":result}

@router.get("/get/{id}",status_code=status.HTTP_302_FOUND,response_model=review_out)
def get_review(id,db:Session=Depends(get_db)):
    result = db.query(Review).filter(Review.Id==id).first()
    if not result :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="These review is not found")
    print(result.__dict__)
    return result

@router.get("/getall/",status_code=status.HTTP_302_FOUND,response_model=List[review_out])
def get_review(db:Session=Depends(get_db)):
    result = db.query(Review).all()
    if not result :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="There is not review")
    print(result)
    return result


@router.delete("/delete/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_review(id:int,db:Session=Depends(get_db),userid:int=Depends(get_current_user)):
    result = db.query(Review).filter(Review.Id==id)
    if not result.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="These review is not found")
    
    owner_id = result.first().user_id
    if owner_id != userid.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    result.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/update/{id}",status_code=status.HTTP_200_OK,response_model=review_out)
def update_review (id:int,resv:review_in,db:Session=Depends(get_db),userid:int=Depends(get_current_user)):
    
    result = db.query(Review).filter(Review.Id==id)
    if not result.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="These review is not found")
    
    owner_id = result.first().user_id
    if owner_id != userid.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    resv.user_id = userid.id
    resv = resv.dict()
    result.update(resv,synchronize_session=False)
    db.commit()
    return  result.first()
