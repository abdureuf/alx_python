"""
import the the class Base from the package models.base.
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class.

    This class represents a rectangle and inherits from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ 
          Initialize a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional):  Defaults to 0.
            y (int, optional):  Defaults to 0.
            id (int, optional): Optional id for the Rectangle object. If provided, assign it to the id attribute.
                      Otherwise, increment __nb_objects and assign the new value to the id attribute.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for the width attribute.
          because of the variable is private, we use getter to access
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute.
          because of the variable is private, we use setter to access and set
        """
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute.
         because of the variable is private, we use getter to access
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute.
           because of the variable is private, we use setter to access and set
        """
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute.
           because of the variable is private, we use setter to access
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute.
           because of the variable is private, we use setter to access and set
        """
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute.
          because of the variable is private, we use setter to access 
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute.
         because of the variable is private, we use setter to access and set
        """
        self.__y = value