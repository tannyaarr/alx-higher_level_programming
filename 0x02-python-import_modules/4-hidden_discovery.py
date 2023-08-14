#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    _dir = dir(hidden_4)
    for i in _dir:
        if i[:2] != "__":
            print(i)
