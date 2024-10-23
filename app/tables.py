from app.db import Base 
from sqlalchemy import Column,Integer,String,Date,ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
class restaurant(Base):
    __tablename__ = "restaurant"
    Id= Column(Integer,primary_key=True,nullable=False)
    name = Column(String,nullable=False)
    address = Column(String,nullable=False)
    phone_number =Column(Integer,nullable=False)
    Cusine_type = Column(String,nullable=False)
    Website = Column(String,nullable=False)
    created_at =  Column(Date, nullable=False, server_default=text("CURRENT_DATE"))
    owned_by =Column(Integer,ForeignKey("user.Id",ondelete="CASCADE"),nullable=False)
    user = relationship("user")

class user(Base):
    __tablename__ = "user"
    Id= Column(Integer,primary_key=True,nullable=False)
    name = Column(String,nullable=False)
    email= Column(String,nullable=False)
    phone_number =Column(Integer,nullable=False)
    password= Column(String,nullable=False)
    time = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("now()"))

class Reservation(Base):
    __tablename__ ="reservation"
    Id = Column(Integer,primary_key=True,nullable=False)
    creator = Column(Integer,ForeignKey("user.Id",ondelete="CASCADE"),nullable=False)
    at_restaurant =Column(Integer,ForeignKey("restaurant.Id",ondelete="CASCADE"),nullable=False)
    date = Column(Date, nullable=False, server_default=text("CURRENT_DATE"))
    created_at= Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("now()"))
    number_of_people = Column(Integer,nullable=False)
    user = relationship("user")
    restaurant = relationship("restaurant")

class Review(Base):
    __tablename__ ="review"
    Id = Column(Integer,primary_key=True,nullable=False)
    user_id = Column(Integer,ForeignKey("user.Id",ondelete="CASCADE"),nullable=False)
    at_restaurant = Column(Integer,ForeignKey("restaurant.Id",ondelete="CASCADE"),nullable=False)
    Rating = Column(Integer,nullable=False)
    comment = Column(String,nullable=False)
    created_at =Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("now()"))
    user = relationship("user")
    restaurant = relationship("restaurant")
