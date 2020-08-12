#!/usr/bin/python3
"""
This module defines class Review that inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Initialize class Review with attributes
        place_id: (str) place id
        user_id: (str) user id
        text: (str)
    """
    place_id = ""
    user_id = ""
    text = ""
