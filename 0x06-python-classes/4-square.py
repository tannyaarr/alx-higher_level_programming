#!/usr/bin/python3
"""Define the class Square based by 3-square.py"""


class Square:
    """This class represents a square"""


    def __init__(self, size=0):
        """
        Initializes a Square with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        Returns:
            None
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the current size of the square.

        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size for the square.

        Raises:
            TypeError: if the value is not an integer.
            ValueError: if the value is less than 0

        Returns:
            None
        """

        if type(value) is not int:
            raise TypeError("size must be integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculate and return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
