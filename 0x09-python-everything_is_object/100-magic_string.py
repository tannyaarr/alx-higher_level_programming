#!/usr/bin/python3
def magic_string():
    return '\n'.join(f"BestSchool{'', ', BestSchool' * i}" for i in range(10))
