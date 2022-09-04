#!/usr/bin/python3

"""parent class to be inherited"""

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """Defines all attributes and methods"""

    def __init__(self, *args, **kwargs):
        """initializes all attributes"""

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.update_at = self.created_at
            storage.new(self)

        else:
            f = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'update-at':
                    value = datetime.strptime(kwargs[key], f)
                if key != '__class__':
                    setattr(self, key, value)
        
    def __str__(self):
        """returns class name, id and attribute dictionary"""
        class_name = "[" + self.__class__.__name__ + "]"
        dict = {k:v for (k, v) in self.__dict__.items() if (not v) is False}
        return class_name + "(" + self.id + ")" + str(dict)


    def save(self):
        """updates and save the last update time"""
        self.update_at == datetime.now()
        storage.save()

    def to_dict(self):
        """creates a new dictionary, adding items/key and\
             returning datetimes converted to strings"""
        new_dict = {}

        for key, values in self.__dict__.items():
            if key == "created_at" or key == "update-at":
                new_dict[key]= values.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not values:
                    pass
                else:
                    new_dict = values

        new_dict['__class__'] = self.__class__.__name__

        return new_dict
