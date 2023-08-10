"""
import the the class Rectangle from the package models.rectangle.
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    The class name Square that inheretes from Rectangle class.
    it contains __init__method,setter and getter methods.

    """
    def __init__(self, size, x=0, y=0, id=None):
       """
         Initializes a Square instance.
         Args:
            size (int): The size of the square.
            x (int): Default is 0.
            y (int):  Default is 0.
            id (int): The id of the square. Default is None.
       """
    
       super().__init__(size, size, x, y, id)
       

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Returns:
            str: A string in the format [Square] (<id>) <x>/<y> - <size>.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
         Gets the size of the square.
         Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        Args:
            value (int): The size of the square.
        """
    
        self.width = value
        self.height = value