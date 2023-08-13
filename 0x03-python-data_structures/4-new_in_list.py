#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_my_list = my_list[:]
    if idx < 0 or idx >= len(new_my_list):
        return(new_my_list)
    new_my_list[idx] = element
    return(new_my_list)
