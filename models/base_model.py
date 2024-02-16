from datetime import datetime
# BaseModel Class

class BaseModel():
    """
    initializing constructor
    Arguments:
        id: id of type int
        created_at: Time created
        updated_at: Time updated
    """
    def __init__(self, id, created_at, updated_at):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
    
    def __str__(self):
        return self.__class__.__name__(), self.id, self.__dict__
    
    #public instance method save()
    def save(self):
        """updates public instance attribute created_at"""
        self.updated_at = datetime.now()
          
    #to_dict(self) publiic instance methods
    def to_dict(self):
        return self.__dict__(__class__)