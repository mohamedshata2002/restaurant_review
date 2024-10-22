from app.db import Base 
from sqlalchemy import Column,Integer,String,Date
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

class restaurant(Base):
    __tablename__ = "restaurant"
    Id= Column(Integer,primary_key=True,nullable=False)
    name = Column(String,nullable=False)
    address = Column(String,nullable=False)
    phone_number =Column(Integer,nullable=False)
    Cusine_type = Column(String,nullable=False)
    Website = Column(String,nullable=False)
    created_at =  Column(Date, nullable=False, server_default=text("CURRENT_DATE"))

class user(Base):
    __tablename__ = "user"
    Id= Column(Integer,primary_key=True,nullable=False)
    name = Column(String,nullable=False)
    email= Column(String,nullable=False)
    phone_number =Column(Integer,nullable=False)
    password= Column(String,nullable=False)
    time = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("now()"))