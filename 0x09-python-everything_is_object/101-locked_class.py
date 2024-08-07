#!/usr/bin/python3

"""
LockedClass module
"""

class LockedClass:
    """
    LockedClass class preventing users from creating instances __slots__
    """
    __slots__ = ['first_name']

