#!/usr/bin/python3

from models.base_model import BaseModel

#Amenity child class inherits from BaseMOdel base class
class Amenity(BaseModel):
    """public class attribute"""
    name: str = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)