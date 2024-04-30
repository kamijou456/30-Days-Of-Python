import os
import sys
import statistics
import math
import string
import random
from modules_EX_1 import*

# 1 

def list_of_hexa_colors(num):

    hexa_lst = []

    for i in range(num):

        hexa_str = "#"

        for i in range(6):

            hexa_str += random.choice(string.hexdigits[0:16])

        hexa_lst.append(hexa_str)

    return hexa_lst

# print(list_of_hexa_colors(5))

# 2

def list_of_rgb_colors(num):

    rgb_lst = []

    [rgb_lst.append(rgb_color_gen()) for i in range(num)]

    return rgb_lst

# print(list_of_rgb_colors(5))

# 3

def generate_colors(format , num):

    number = int(num)

    if format == "hexa":

        output = list_of_hexa_colors(number)

    elif format == "rgb":

        output = list_of_rgb_colors(number)

    else:

        print("invalid format input")

    return output

# print(generate_colors(input("Which number format do you want, hexa, or rgb: ") , input("How many different colors do you want to output: ")))