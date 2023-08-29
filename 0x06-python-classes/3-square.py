#!/usr/bin/python3
"""Define the class Square based on 2-square.py"""


class Square:
    """This class represents a square"""


    def __init__(self, size=0):
        """
        Initializes a Square with an optional size

        Args:
            size (int, optional): The size of the square. Defaults to 0

        Raises:
            TypeError: If the size is not an integer
            ValueError: If the size is less than 0.

        Returns:
            None
        """

        if type(size) is not int:
            raise TypeError("size must not an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculate and return the current square area

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2
