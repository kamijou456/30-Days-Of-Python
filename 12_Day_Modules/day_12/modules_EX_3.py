import os
import sys
import statistics
import math
import string
import random
from modules_EX_1 import*

# 1

num_lst = [1,2,3,4,5,6,7,8,9]

def shuffle_lst(lst):

    random.shuffle(lst)

    return lst

print(shuffle_lst(num_lst))

# 2

def rando_unique():

    lst = [i for i in range(10)]

    random.shuffle(lst)

    return lst[0:7]

print(rando_unique())