#! /usr/bin/env python

"""

"""

from __future__ import division, print_function

def p_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Requirement is not applicable")
    mismatches = 0
    current_lenght = len(str1)
    for a, b in zip(str1, str2):
        if a != b and a != "-" and b != "-":
            mismatches += 1
        if a == "-" or b == "-":
            current_lenght -= 1
    if current_lenght:
        return mismatches / current_lenght
    else:
        raise ValueError("No more string")
