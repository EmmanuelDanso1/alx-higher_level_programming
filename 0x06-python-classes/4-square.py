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
        initializes the square with the given size
        Args:
            size(int, optional): The size of the square with 0 as default
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
    def size(self, value):
        """
        Sets the size of the Square
        Args:
            value(int): The size of the square
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
            int: The area of the square
        """
        return self.__size * self.__size

