#!/usr/bin/python3
"""Square module"""
class Square:
    """
    A class that defines a square with a private instance attribute size
    Attributes:
        __size(int): the size of the square
    """
    def __init__(self, size=0):
        """
        initializes the square with the given size
        Args:
            size(int, optional): the sqize of the square with 0 as default
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        self.size = size
    @property
    def size(self):
        """
        Retrieves the size of the square
        Returns:
            int: the size of the square
        """
        return self.__size

    @size.setter
    def size(size, value):
        """
        Sets the size of the square
        Args:
            value(int): the size of the square
        Raises:
                TypeError: if size is not an integer
                ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """
        Calculates the area of the square
        Returns:
            int: the area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints in standard output the square with character #
        if size is equal to 0. prints an empty line
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)


