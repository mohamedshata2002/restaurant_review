from pydantic import BaseModel ,EmailStr
from datetime import date ,datetime 
from typing import Optional

 
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
     owned_by :Optional[int] =None
     pass



class user(BaseModel):
    name:str
    phone_number:int
    class Config:
        from_attributes = True  
    

class user_in(user):
    email:EmailStr
    password:str

class user_out(user):
    Id:int
    time: datetime

class restaurant_out(restaurant):
    user : user_out
    Id :int

class Token_data(BaseModel):
    id :Optional[int]=None 


class Token_response (BaseModel):
    token: str
    token_type:str
    
    class Config:
        orm_mode = True
