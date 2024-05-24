#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_set = set()
    if my_list:
        for items in my_list:
            uniq_set.add(items)
    return sum(uniq_set)
