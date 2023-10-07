#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        max_int = my_list[0]
        for j in my_list:
            if j > max_int:
                max_int = j
                return max_int
