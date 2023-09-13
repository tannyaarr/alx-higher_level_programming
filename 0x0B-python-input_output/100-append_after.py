#!/usr/bin/python3
"""Defines the append search and update"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line a text to a file after each line containing
        a specific string"""

    if not filename:
        return

    with open(filename, 'r', encoding='utf-8') as f:
            lines = f.realines()

    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string + '\n')

#test
#!/usr/bin/python3
append_after = __import__('100-append_after').append_after

append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
