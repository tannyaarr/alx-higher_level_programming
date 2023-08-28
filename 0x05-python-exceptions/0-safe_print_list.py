#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb_print = 0

    try:
        for i in my_list:
            if nb_print < x:
                print(i, end="")
                nb_print += 1
    except:
        pass
    finally:
        print()
    return nb_print
