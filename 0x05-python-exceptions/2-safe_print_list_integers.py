#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in my_list:
            if count < x:
                try:
                    print("{:d}".format(i), end="")
                    count += 1
                except:
                    pass
        print()
        print("nb_print:", count)
    except:
        print()
        print("nb_print:", count)
        raise
