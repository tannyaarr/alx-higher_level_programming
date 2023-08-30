#!/usr/bin/python3
"""Define the class Square based on 5-square.py"""


class Square:
    """This class represents a square."""


    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            postion (tuple, optional): The position of the square. Defaults to (0, 0)

        Raises:
            TypeError: If size is not an integer or if position not a tuple of 2 positive integers
            ValueError: If size is less than 0 or if position values are not positive

        Returns:
            None
        """

        self.size = size
        self.position = position
    

    @property
    def size(self):
        """
        Retrieve the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size
    

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size for the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = value
    

    @property
    def position(self):
        """
        Retrieve the current postion of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position
    

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): The new position of the square

        Raises:
            TypeError: If the value is not a tuple or values inside the tuple are not integers.
            ValueError:If tuple does not contain 2 positive integers

        Returns:
            None
        """

        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise ValueError("position values must be positive")

        self.__position = value



    def area(self):
        """
        Calculate and return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the character #.

        Returns:
            None
        """

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
