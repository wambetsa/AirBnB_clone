#!/usr/bin/python3

from models.base_model import BaseModel

# City child class inherits from BaseModel parent class
class City(BaseModel):
    """public class attributes"""
    state_id: str = ""
    name: str = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)