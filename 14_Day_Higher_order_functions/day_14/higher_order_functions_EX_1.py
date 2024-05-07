import os
import sys
import statistics
import math
import string
import random
from functools import reduce as rd

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Map will call a function for each iterable in a list. Filter will use a boolean returned function value and make a list of based on if the values in the original iterable pass the functions test. Reduce is similar to filter but returns only one value instead of a list of values.

# 2 Higher order functions take functions as parameters. Closure is when a function is nested inside of an outer function. Decorator allows the programmer to call a higher order function to process the function.

# 3

def square(num):
    return num ** 2

def evens(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
def add_two_nums(x,y):
    return int(x) + int(y)

square_map = map(square , numbers)

lst_filter = filter(evens , numbers)

reduce_obj = rd(add_two_nums, numbers)

# print(list(square_map))

# print(list(lst_filter))

# print(reduce_obj)

# 4

# [print(i) for i in countries]

# 5

# [print(i) for i in names]

# 6

# [print(i) for i in numbers]


