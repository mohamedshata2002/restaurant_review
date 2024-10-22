from pydantic import BaseModel ,EmailStr
from datetime import date ,datetime


 
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
    Id :int

class user(BaseModel):
    name:str
    phone_number:int
    

class user_in(user):
    email:EmailStr
    password:str

class user_out(user):
    Id:int
    created_at: datetime