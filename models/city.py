#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import place


class City(BaseModel, Base):
    """ The city class, contains state ID and name
     and inherits from BaseModel and Base """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

    state = relationship("State", back_populates="cities")
    places = relationship("Place", backref="cities", cascade='all,
                          delete, delete-orphan')
