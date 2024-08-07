#!/usr/bin/python3
"""
A function that adds two integers and returns the addition
"""
def add_integer(a, b=98):
    """
    returns the addition of two arguments
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        if type(a) is float:
            a = int(a)
        if type(b) is float:
            b = int(b)
        return a + b

