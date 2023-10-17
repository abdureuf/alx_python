#!/usr/bin/python3
"""
This module defines the Rectangle class.
"""
from .5-base_geometry import BaseGeometry

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
    