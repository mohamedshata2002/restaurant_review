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