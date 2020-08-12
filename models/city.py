#!/usr/bin/python3
"""
This module defines class City that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Initialize class City with attributes
        state_id: (str) refers to State.id
        name: (str) name of the city
    """
    state_id = ""
    name = ""
