#!/usr/bin/python3
"""Square module"""
class Square:
    """
    A class that defines a square with a private instance
    attribute
    Attributes:
        __size(int): The size of square
    """
    def __init__(self, size):
        """
        Initializes a square with a given size
        Args:
            size(int): size of the square
        """
        self.__size = size

