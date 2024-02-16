#!/usr/bin/python3

from models.base_model import BaseModel

#State child class inherits from BaseModel parent class
class State(BaseModel):
    """public class atribute name: empty string"""
    name: str = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)