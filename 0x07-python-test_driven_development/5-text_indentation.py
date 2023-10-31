#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    lines = []

    for char in text:
        if char in ['.', '?', ':']:
            lines.append("")
        else:
            if len(lines) == 0:
                lines.append(char)
            else:
                lines[-1] += char

    for line in lines:
        print(line.strip())
