"""
import the the class Rectangle from the package models.rectangle.

"""
from models.rectangle import Rectangle
class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square (width and height).
            x (int): The x-coordinate of the square's position (default: 0).
            y (int): The y-coordinate of the square's position (default: 0).
            id (int): The id of the square (default: None).
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Overrides the __str__ method to return a string representation of the Square instance.

        Returns:
            str: The string representation of the Square instance.
        """
        return f"[Square] ({self.id}) {self._Rectangle__x}/{self._Rectangle__y} - {self._Rectangle__width}"

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

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square.

        Args:
            args: Variable length argument list.
            kwargs: Arbitrary keyword arguments.
        """
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the square.

        Returns:
            dict: A dictionary containing the square attributes.
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.width ** 2

    def display(self):
        """
        Displays the square using '#' characters.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)