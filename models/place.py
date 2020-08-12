#!/usr/bin/python3
"""
This module defines class Place that inherits from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Initialize class Place with attributes
        city_id: city
        user_id: user's id
        name: name
        description: description
        number_rooms: number of rooms
        number_bathrooms: number of bathrooms
        max_guest: maximum guest
        price_by_night: price by night
        latitude: latitude
        longitude: longitud
        amenity_ids: amentity id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
