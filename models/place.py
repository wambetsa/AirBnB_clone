#!/usr/bin/python3

from models.base_model import BaseModel

#Child class Place inherits from parent/base class BaseModel
class Place(BaseModel):
    """public class attributes"""
    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_quests: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: list = []

    """init constructor"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)