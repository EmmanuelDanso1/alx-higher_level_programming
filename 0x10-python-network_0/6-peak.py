#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers with DSA
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers (list): List of integers to find peak in.
    Returns:
        Peak of the list_of_integers(int) or None if the list is empty.
    """
    list_len = len(list_of_integers)

    if list_len == 0:
        return None

    lft = 0
    rgt = list_len - 1

    while lft < rgt:
        mid = (lft + rgt) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            lft = mid + 1
        else:
            rgt = mid

    return list_of_integers[lft]

