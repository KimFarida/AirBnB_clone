#!/usr/bin/python3
"""unittest place.py"""

import unittest
from models.place import Place
import datetime


class TestPlace(unittest.TestCase):
    """tests instances and methods from amenity class"""

    place = Place()

    def test_class_exists(self):
        self.assertEquals(str(type(self.p)), "<class 'models.place.Place'>")

    def test_user_inheritance(self):
        """testing subclass BaseModel"""
        self.assertIsInstance(self.p, Place)

    def testHasAttributes(self):
        """checking if attributes exist"""
        self.assertTrue(hasattr(self.p, 'city_id'))
        self.assertTrue(hasattr(self.p, 'user_id'))
        self.assertTrue(hasattr(self.p, 'name'))
        self.assertTrue(hasattr(self.p, 'description'))
        self.assertTrue(hasattr(self.p, 'number_rooms'))
        self.assertTrue(hasattr(self.p, 'number_bathrooms'))
        self.assertTrue(hasattr(self.p, 'max_guest'))
        self.assertTrue(hasattr(self.p, 'price_by_night'))
        self.assertTrue(hasattr(self.p, 'latitude'))
        self.assertTrue(hasattr(self.p, 'longitude'))
        self.assertTrue(hasattr(self.p, 'amenity_id'))
        self.assertTrue(hasattr(self.p, 'id'))
        self.assertTrue(hasattr(self.p, 'created_at'))
        self.assertTrue(hasattr(self.p, 'updated_at'))