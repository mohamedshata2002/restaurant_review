from fastapi import APIRouter ,HTTPException ,Response, status
from app.schema import reservation_in , reservation_out
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db import get_db 
from typing import List
from app.tables import Reservation ,restaurant
from app.othen import get_current_user
router = APIRouter(prefix="/reservation",tags=["reservation"])

@router.post('/create',status_code = status.HTTP_201_CREATED)
def create_reservation(resv:reservation_in,db:Session=Depends(get_db),userid:int=Depends(get_current_user)):
    id = resv.at_restaurant
    res = db.query(restaurant).filter(restaurant.Id==id).first()
    if not res:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="These restuarant is not found")
    resv.creator = userid.id
    result = Reservation(**resv.dict())
    db.add(result)
    db.commit()
    db.refresh(result)
    return{"result":result}

@router.get("/get/{id}",status_code=status.HTTP_302_FOUND,response_model=reservation_out)
def get_reservation(id,db:Session=Depends(get_db)):
    result = db.query(Reservation).filter(Reservation.Id==id).first()
    if not result :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="These reservation is not found")
    print(result.__dict__)
    return result

@router.get("/getall/",status_code=status.HTTP_302_FOUND,response_model=List[reservation_out])
def get_reservation(db:Session=Depends(get_db)):
    result = db.query(Reservation).all()
    if not result :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="There is not reservation")
    print(result)
    return result


@router.delete("/delete/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_reservation(id:int,db:Session=Depends(get_db),userid:int=Depends(get_current_user)):
    result = db.query(Reservation).filter(Reservation.Id==id)
    if not result.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="These reservation is not found")
    
    owner_id = result.first().creator
    if owner_id != userid.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    result.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/update/{id}",status_code=status.HTTP_200_OK,response_model=reservation_out)
def update_reservation (id:int,resv:reservation_in,db:Session=Depends(get_db),userid:int=Depends(get_current_user)):
    
    result = db.query(Reservation).filter(Reservation.Id==id)
    if not result.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="These reservation is not found")
    
    owner_id = result.first().creator
    if owner_id != userid.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    resv.creator = userid.id
    resv = resv.dict()
    result.update(resv,synchronize_session=False)
    db.commit()
    return  result.first()
