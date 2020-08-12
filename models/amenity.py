#!/usr/bin/python3
"""
This module defines class Amenity that inherits from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Initialize class Amenity with attribute
        name: (str) name of the amenity
    """
    name = ""
