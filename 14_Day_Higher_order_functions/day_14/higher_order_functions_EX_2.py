import os
import sys
import statistics
import math
import string
import random
from functools import reduce as rd
from higher_order_functions_EX_1 import countries, names, numbers, square, evens

# 1

def uppercase(str):
    return str.upper()

upper_countries = map(uppercase, countries)

# 2

square_nums = map(square, numbers)

# 3

upper_names = map(uppercase, names)

# 4

def land_filter(count):

    if "land" in count:
        return False
    else:
        return True
    
filter_land = filter(land_filter, countries)

# 5

def short_country_name(count):
    if len(count) == 6:
        return False
    else:
        return True
    
six_char_country_filter = filter(short_country_name, countries)

# 6

def short_country_name_gtr(count):
    if len(count) >= 6:
        return False
    else:
        return True
    
six_char_and_up_filter = filter(short_country_name_gtr, countries)

# 7 

def country_name_starts_e(count):
    if count.startswith() == "E":
        return False
    else:
        return True
    
country_starts_e_filter = filter(country_name_starts_e, countries)

# 8 

chain_lst = list(filter(evens, list(map(square, numbers))))

# 9

def get_string_lsts(lststr):

    lst = []

    [lst.append(i) for i in lststr if type(i) == str]

    return lst

# Exercises are getting redundant. I have already written algorithims for these prompts.