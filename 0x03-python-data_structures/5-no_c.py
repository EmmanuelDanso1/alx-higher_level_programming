#!/usr/bin/python3
def no_c(my_string):
    if my_string[:]:
        new_str = my_string.translate({ord("c"): None})
        another_str = new_str.translate({ord("C"): None})
        return another_str
    else:
        return my_string
