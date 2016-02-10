#! /usr/bin/env python

from __future__ import division, print_function


def my_filter(fn, elements, **kwargs):
    result = []
    for element in elements:
        if fn(element, **kwargs):
            result.append(elements, **kwargs)
    return result
