#!/usr/bin/python3
"""
no import
"""
class BaseGeometry:
    """
    BaseGeometry is a class with area and integer_validator methods.
    """
    
    def area(self):
        """
        Raises an exception when called.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value as an integer.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))