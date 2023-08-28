#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    try:
        for i in range(list_length):
            try:
                a = my_list_1[i] if i < len(my_list_1) else 0
                b = my_list_2[i] if i < len(my_list_2) else 0
                if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                    if b != 0:
                        result.append(a / b)
                    else:
                        result.append(0)
                        print("divison by 0")
                else:
                    result.append(0)
                    print("wrong type")
            except IndexError:
                print("out of range")
    finally:
        return result
