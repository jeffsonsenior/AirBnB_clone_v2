#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Foreignkey
from sqlalchemy.orm import relationship
from model.place import place

class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    state_id = Column(String(60), Foreignkey("state.id"), nullable=False)
    name = Column(String(128), nullable=False)
    place = relationship("place", cascade="all,delete",brackref='cities')
    state_id = ""
    name = ""
