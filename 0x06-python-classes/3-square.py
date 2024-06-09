#!/usr/bin/python3
"""Square module"""
class Square:
    """
    A class that defines a square with a private instance attribute size
    Attributes:
        __size(int): The size of the square
    """
    def __init__(self, size=0):
        """
        initializes the square with the given
        Args:
            size(int, optional): The size of the square 
            Raises:
                TypeError: If size is not an integer
                ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """
        Calculates the area of the square
        Returns:
            int: the area of the square
        """
        return self.__size * self.__size

