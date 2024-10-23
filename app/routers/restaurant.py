from fastapi import APIRouter ,HTTPException ,Response, status
from app.schema import restaurant_in , restaurant_out
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db import get_db 
from typing import List
from app.tables import restaurant
from app.othen import get_current_user
router = APIRouter(prefix="/restaurant",tags=["restaurant"])

@router.post('/create',status_code = status.HTTP_201_CREATED)
def create_restaurant(rest:restaurant_in,db:Session=Depends(get_db),userid:int=Depends(get_current_user)):
    rest.owned_by = userid.id
    result = restaurant(**rest.dict())
    db.add(result)
    db.commit()
    db.refresh(result)
    return{"result":result}

@router.get("/get/{id}",status_code=status.HTTP_302_FOUND,response_model=restaurant_out)
def get_restuarant(id,db:Session=Depends(get_db)):
    result = db.query(restaurant).filter(restaurant.Id==id).first()
    if not result :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="These restuarant is not found")
    print(result)
    return result

@router.get("/getall/",status_code=status.HTTP_302_FOUND,response_model=List[restaurant_out])
def get_restuarant(db:Session=Depends(get_db)):
    result = db.query(restaurant).all()
    if not result :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="There is not restaurent")
    print(result)
    return result


@router.delete("/delete/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_restaurent(id:int,db:Session=Depends(get_db),userid:int=Depends(get_current_user)):
    result = db.query(restaurant).filter(restaurant.Id==id)
    if not result.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="These restuarant is not found")
    
    owner_id = result.first().owned_by
    if owner_id != userid.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    result.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/update/{id}",status_code=status.HTTP_200_OK,response_model=restaurant_out)
def update_restaurant (id:int,rest:restaurant_in,db:Session=Depends(get_db),userid:int=Depends(get_current_user)):
    
    result = db.query(restaurant).filter(restaurant.Id==id)
    if not result.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="These restuarant is not found")
    
    owner_id = result.first().owned_by
    if owner_id != userid.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    rest.owned_by = userid.id
    rest = rest.dict()
    result.update(rest,synchronize_session=False)
    db.commit()
    return  result.first()
