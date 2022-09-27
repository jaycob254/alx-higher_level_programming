#!/usr/bin/python3
"""
Contains the number_of_lines function
"""


def number_of_lines(filename=""):
    """returns the number of lines of a text file"""
    with open(filename, 'r', encoding='utf8') as f:
        k = 0
        for line in f:
            k += 1
        return k
