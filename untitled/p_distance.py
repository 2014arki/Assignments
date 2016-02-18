#! /usr/bin/env python

"""

"""

from __future__ import division, print_function

def p_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Requirement is not applicable")
    mismatches = 0
    p_distance_value = mismatches % len(str1)
    for a, b in zip((str1, str2)):
        if a != b and a != "-" and b != "-":
            mismatches += 1
        if a == b:
            next(iter)
        if a == "-" or b == "-":
            str1.split(a) and str2.split(b)
    if str1 and str2 and mismatches:
        return p_distance_value
