#!/usr/bin/python3

"""
LockedClass module with no class or object attribute, that prevents the user
from dynamically creating new instance attributes
"""

class LockedClass:
    """
    LockedClass class preventing users from creating instances __slots__
    """
    __slots__ = ['first_name']

