import os
import sys
import statistics
import math
import string
import random
from datetime import *

# 1

now = datetime.now()

print(now)

print(now.day)

print(now.month)

print(now.year)

print(now.hour)

print(now.minute)

print(now.timestamp())

# 2

formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")

print(formatted_date)

# 3

date_string = "5 December, 2019"

str2time = datetime.strptime(date_string, "%d %B, %Y")

print(str2time)

# 4

new_years = datetime(2025, 1, 1)

new_years_delta = new_years - now

print(new_years_delta)

# 5 

timestamp_start = datetime(1970, 1, 1)

timestamp_delta = now - timestamp_start

print(timestamp_delta)