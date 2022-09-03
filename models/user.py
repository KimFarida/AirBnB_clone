#!/usr/bin/python3
"""user creation class"""
import email
from models.base_model import BaseModel


class User(BaseModel):
    """defining the user parameters"""
    first_name = ""
    last_name = ""
    email = ""
    password = ""
