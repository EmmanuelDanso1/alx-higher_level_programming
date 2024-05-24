#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = []
    if a_dictionary:
        for k, v in a_dictionary.items():
            keys.append(k)

        keys.sort()
        for items in keys:
            print("{}: {}".format(items, a_dictionary[items]))
