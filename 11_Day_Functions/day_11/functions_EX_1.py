import numpy as np

# 1

'''

def add_two_numbers(par1,par2):
    tot = par1 + par2
    return tot

print(add_two_numbers(3,4))

'''

# 2

'''

def area_of_circle(radius):
    area = np.pi * (radius**2)
    return area

print(area_of_circle(2))

'''

# 3

'''

def add_all_nums(*nums):
    total = 0
    for num in nums:
        if type(num) != int:
            print('item in the list is not a number')
        else:
            total += num
    return total

print(add_all_nums(1,2,3,4,'lol',6,7,8,9))

'''

# 4

'''

Temp = int(input('Enter tempurature:'))

def convert_temp_from_cTOf(temp):
    Faren = (temp * (9/5)) + 32
    outputTemp = str(Faren) + ' degrees Fahrenheit!'
    return outputTemp

print(convert_temp_from_cTOf(Temp))

'''

# 5

'''

Month = int(input('Enter the number of a month that you want to check the which season it belongs in: '))

def check_season(month):
    season = ''
    if month in [12,1,2]:
        season = 'Winter'
    elif month in [3,4,5]:
        season = 'Spring'
    elif month in [6,7,8]:
        season = 'Summer'
    elif month in [9,10,11]:
        season = 'Fall'
    else:
        season = 'Invalid input!'
    
    return season

print(check_season(Month))

'''

# 6

'''

cartPoints = {'point1x':float(input('Enter value of x at point 1: ')), 'point1y':float(input('Enter value of y at point 1: ')), 'point2x':float(input('Enter value of x at point 2: ')), 'point2y':float(input('Enter value of y at point 2: '))}

def calculate_slope(points):
    
    slope = (points['point2y'] - points['point1y']) / (points['point2x'] - points['point1x'])

    return slope

print(calculate_slope(cartPoints))

'''

# 7

