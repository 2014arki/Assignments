#! /usr/bin/env python

from __future__ import division, print_function



# task 3


def my_map(fn, elements, **kwargs):
     result = []
     for element in elements:
         result.append(fn(element, **kwargs))
     return result



def my_filter(fn, elements, **kwargs):
    result_filter = []
    for element in elements:
        if fn(element, **kwargs):
            result_filter.append(fn(element, **kwargs))
    return result_filter


# task 4


def calculate(numbers, operators):
     if len(numbers) != len(operators) + 1:
         raise ValueError ("Check parameters")

     operation_dictionary = {
    "+": operator.add(),
    "*": operator.mul(),
    "/": operator.div(),
    "-": operator.sub()
     }
     numbers_iterator = iter(numbers)
     acc = next(numbers_iterator)
     for num, oper in zip(numbers_iterator, operators):
         oper_func = operation_dictionary.get(oper)
         if not oper_func:
            raise ValueError("Operation {} is not usable".format(oper))
     acc = oper_func(acc, num):
        return acc


# task 5


def evaluate_string(evaluate):
    operation_dictionary = {
    "+": operator.add,
    "-": operator.sub
    }
    numbers_ = []
    current_numbers_ = []
    operations = []
    for element in evaluate:
        if evaluate.isdigit():
            current_numbers_.append(element)
        if not element.isdigit:
            whole_number = "".join(current_numbers_)
            numbers_.append(int(whole_number))
            current_numbers_ = []
            if element in operation_dictionary:
                operations.append(element)
            if element != " ":
                raise ValueError("Unsupported operation")
            else:
                continue
    if numbers_ and operations:
        calculation_ = calculate(numbers_, operations)
        return calculation_




