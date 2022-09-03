#!/usr/bin/python3
"""a class to serialize instances to JSON file\
     and deserializes JSON file to instances"""
import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """function to return the dictionary _objects"""
        return FileStorage.__objects

    def new(self, obj):
        """setting in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.name__+ "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        dictionary = {}

        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()

            with open(FileStorage.__file_path, 'w') as f:
                json.dump(dictionary, f)

    def reload(self):
        """deserializes __objects from the JSON file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review
        dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,\
            'City': City, 'Amenity': Amenity, 'State':State,\
                'Review': Review}

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    self.new(dct[value['__class__']](**value))