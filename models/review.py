from models.base_model import BaseModel

#child class Review inherits from base/parent class BaseModel
class Review(BaseModel):
    """public class attributes"""
    place_id: str = ""
    user_id: str = ""
    text: str = ""

    """init constructor"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)