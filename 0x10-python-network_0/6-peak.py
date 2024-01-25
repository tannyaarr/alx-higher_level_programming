#!/usr/bin/python3

def find_peak(list_of_integers):
    """
    find a peak ina list of unsorted integers

    args:
    - list_of_integers: of a list of unsorted integers

    returns
    - the peak elements(s) in the list.
    """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return list_of_integers[low]
