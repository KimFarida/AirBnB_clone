#!/usr/bin/python3
"""Module for class FileStorage"""

import json
import os


class FileStorage:

    """For the Serialization and Deserialization of Base Classes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        to_dict = {}
        for key, obj in FileStorage.__objects.items():
            to_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(to_dict, f, indent=4)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as f:
                _dict = json.load(f)

            new_dict = {}
            for obj_name, obj_details in _dict.items():
                obj = BaseModel(**obj_details)
                new_dict[obj_name] = obj

            FileStorage.__objects = new_dict
        except FileNotFoundError:
            pass
