#!/usr/bin/env python


from __future__ import division, print_function


def my_max_(*args):

    arg_left = 'a'
    arg_right = 'b'

    if len(*args) == 1 and args not in list or tuple:
      raise TypeError("The object {} of {} is not support {}"
                      ", {} type". format(args, my_max_, not list, not tuple))
    if len(*args) > 1 and args is not int:
        raise ValueError("This object {} of {} is not support {}"
                         " value". format(args, my_max_, not int))
    if ('a' % 'b') == 1:
        return None
    if ('a' % 'b') > 1:
        return 'a'
    return 'b'
