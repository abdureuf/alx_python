#!/usr/bin/python3
"""
This module defines the Rectangle class.
"""

class BaseGeometry:
    """
    BaseGeometry is a class with area and integer_validator methods.
    """
    def __dir__(self):
        """
        Customizes the behavior of dir() method.
        """
        attrs = set(dir(type(self))) | set(self.__dict__) | set(dir(BaseGeometry))
        attrs = attrs - {'__init_subclass__'}
        attrs = [attr for attr in attrs if not attr.startswith('__')]
        return sorted(attrs)

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


class Rectangle(BaseGeometry):
    """
    Rectangle is a class that inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height.
        """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
