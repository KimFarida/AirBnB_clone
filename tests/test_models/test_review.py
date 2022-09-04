#!/usr/bin/python3
"""unittest for review.py"""
import unittest
from models.review import Review
import datetime


class TestReview(unittest.TestCase):
    """tests instances and methods from review class"""

    r = Review()

    def test_class_exists(self):
        """testing if the class exists"""
        res = "<class 'models.review.Review'>"
        self.assertEqual(str(type(self.r)), res)

    def test_user_inheritance(self):
        """testing if the Review has a subclass BaseModel"""
        self.assertIsInstance(self.r, Review)