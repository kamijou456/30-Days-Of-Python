# modules_EX_1.py file
import os
import sys
import statistics
import math
import string
import random

# 1

def random_user_id(num):

    user_id = ""

    for i in range(num):

        let = random.choice(string.ascii_letters + string.digits)

        user_id += let

    return user_id

# print(random_user_id(6))

# 2

def user_id_gen():

    l_id = int(input("Enter number for length of id's: "))

    num_id = int(input("Enter number of id's to be made: "))

    id_lst = []

    [id_lst.append(random_user_id(l_id)) for i in range(num_id)]
    
    return [i for i in id_lst]

# [print(i) for i in user_id_gen()]

# 3

def rgb_color_gen():

    rgb_lst = []

    [rgb_lst.append(random.randint(0,255)) for i in range(3)]

    rgb_output = "rgb" + str(tuple(rgb_lst))

    return rgb_output

# print(rgb_color_gen())