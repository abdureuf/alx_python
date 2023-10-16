#!/usr/bin/python3
"""
no import
"""
class BaseGeometry:
    """
    BaseGeometry is a class with an area method that raises an exception.
    """
    def area(self):
        """
        Raises an exception when called.
        """
        raise Exception("area() is not implemented")