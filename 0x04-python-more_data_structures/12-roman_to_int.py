#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rev_str = list(reversed(roman_string))
    results = roman_dict[rev_str[0]]
    i = 0

    while i < (len(rev_str) - 1):
        if rev_str[i] in roman_dict.keys():
            if roman_dict[rev_str[i + 1]] >= roman_dict[rev_str[i]]:                results += roman_dict[rev_str[i + 1]]
            else:
                results -= roman_dict[rev_str[i + 1]]
        i += 1
    return(results)

