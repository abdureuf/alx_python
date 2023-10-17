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
        """
        from super class import value
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        # self.id = id

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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must > 0")
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    def area(self):
        """
           Returns the area of the Rectangle instance.
           The area is calculated by multiplying the width and height of the rectangle.
        """
        return self.__width * self.__height    

    def display(self):
        """
             Prints a visual representation of the Rectangle instance.
             Prints the rectangle by repeating the '#' character 'self.__width' times for each row,
             repeating the rows 'self.__height' times, and taking into account the 'x' and 'y' coordinates.
        """
        for _ in range(self.__y):
          print()
        for _ in range(self.__height):
         print(" " * self.__x + "#" * self.__width)
    def __str__(self):
        """
           Returns a string representation of the Rectangle instance.
           The string has the format '[Rectangle] (<id>) <x>/<y> - <width>/<height>'.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)        

    def update(self, *args,**kwargs):
       """
        Updates the attributes of the Rectangle instance.

        The arguments are assigned in the following order:
        1st argument: id attribute
        2nd argument: width attribute
        3rd argument: height attribute
        4th argument: x attribute
        5th argument: y attribute
        2nd update:
        The arguments can be passed as key-value pairs in **kwargs, where each key
        represents an attribute of the Rectangle instance.
       """
       if args:
           if len(args) >= 1:
               self.id = args[0]
           if len(args) >= 2:
               self.width = args[1]
           if len(args) >= 3:
               self.height = args[2]
           if len(args) >= 4:
               self.x = args[3]
           if len(args) >= 5:
             self.y = args[4]

       else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]


