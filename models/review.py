#!/usr/bin/python3
"""defining the review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """defining the review parameters"""
    place_id = ""
    user_id = ""
    text = ""