from models.base_model import BaseModel

#user class inherits from BaseModel Class
class User(BaseModel):
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""

    def __init__(self, email="", password="", first_name="", last_name="", *args, **kwargs):
        """use super() to inherit super class/parent class arguments"""
        super().__init__(*args, **kwargs)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name