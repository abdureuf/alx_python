"""
The class is in the package of models name
"""
class Base:
    """
    Base class

    This class manages the id attribute for all other classes in the project.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base object.

        Args:
            id (int): Optional id for the Base object. If provided, assign it to the id attribute.
                      Otherwise, increment __nb_objects and assign the new value to the id attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
