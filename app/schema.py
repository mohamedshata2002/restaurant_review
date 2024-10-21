from pydantic import BaseModel
from datetime import date


 
class restaurant(BaseModel):
    name: str
    address: str
    phone_number:int
    Cusine_type:str
    Website:str
    created_at:date
    class Config:
        orm_mode = True

class restaurant_in(restaurant):
     pass

class restaurant_out(restaurant):
    id :int