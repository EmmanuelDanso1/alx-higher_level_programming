#!/usr/bin/python3
""" A square module"""
class Square:
    """
    A class that defines a square with a private instance attribute size
    Attributes:
        __size(int): The size of the square
    """
    def __init__(self, size=0):
        """
        Initialises the square with a given size
        Args:
            size(int, optional): The size of the square, default is 0
        Raises: 
            TypeError: if size is not integer
            ValueError: if size is less that 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
