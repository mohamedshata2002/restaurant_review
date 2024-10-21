from fastapi import APIRouter ,HTTPException ,Response, status
from app.schema import restaurant_in , restaurant_out
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db import get_db 
from typing import List
from app.tables import restaurant

router = APIRouter(prefix="/restaurant",tags=["restaurant"])

@router.post('/create',status_code = status.HTTP_201_CREATED)
def create_restaurant(rest:restaurant_in,db:Session=Depends(get_db)):
    result = restaurant(**rest.dict())
    db.add(result)
    db.commit()
    db.refresh(result)
    return{"result":result}





