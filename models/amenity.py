#!/usr/bin/python3
"""
This module defines class Amenity that inherits from BaseModel
"""
from models.base_model import BaseModel, Base
from models.place import place_amenity
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel):
    """
    Initialize class Amenity with attribute
        name: (str) name of the amenity
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place(amenity))
