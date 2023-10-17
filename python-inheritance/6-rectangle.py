#!/usr/bin/python3
"""
This module defines the Rectangle class.
"""

class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Calculates the area"""
        raise NotImplementedError("area() is not implemented.")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer"""
        if not isinstance(value, int) or value <= 0:
            raise TypeError(f"{name} must be a positive integer.")
        return value


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def __str__(self):
        """Returns a string representation of the object"""
        return f"<Rectangle width={self.__width}, height={self.__height}>"

    def __repr__(self):
        """Returns a string representation of the object"""
        return self.__str__()