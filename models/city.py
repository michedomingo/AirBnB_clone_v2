#!/usr/bin/python3
"""
This module defines class City that inherits from BaseModel
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models.state import State
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    Initialize class City with attributes
        state_id: (str) refers to State.id
        name: (str) name of the city
    """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities", cascade="all, delete")
