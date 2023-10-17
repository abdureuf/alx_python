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
        attrs = attrs - {'__init_subclass__'}  # Exclude '__init_subclass__' method
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
    A class representing a rectangle, inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle in the format [Rectangle] <width>/<height>.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)