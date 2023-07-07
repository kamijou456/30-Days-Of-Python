import numpy

#Day 2 of 30 Days of python programming
first_name = input('Enter First Name: ')
last_name = input('Enter Last Name: ')
full_name = first_name + ' ' + last_name
country = input('Enter Country of Residence: ')
city = input('Enter City of Residence: ')
age = input('Enter Age: ')
year = input('Enter Current Year: ')
is_married = input('Enter yes if you are married or Enter no if you are not married: ')
is_true = 1
is_light_on = 1
firstName, lastName, Age = 'John','Taylor','29'

print('First Name:',first_name)
print(type(first_name))
print('Last Name:',last_name)
print(type(last_name))
print('Full Name:',full_name)
print(type(full_name))
print('Country:',country)
print(type(country))
print('City:',city)
print(type(city))
print('Age:',age)
print(type(age))
print('Current Year:',year)
print(type(year))
print('Marital Status:',is_married)
print(type(is_married))
print('Multi Varible Print:',firstName, lastName, Age)

print('Length of Letters in the First Name:', len(first_name))

answer = input('Which name has largest number of letters? First name has ' + str(len(first_name)) + '. Last name has ' + str(len(last_name)) + ': ')
print('Answer:',answer)

num_one = 5
num_two = 4

print('Practicing Math Functions with 5 as the first number and 4 as the second number.')
ans_add = num_one + num_two
print('Addition:',ans_add)
ans_sub = num_two - num_one
print('Subtraction:',ans_sub)
ans_mul = num_one * num_two
print('Multiplication:',ans_mul)
ans_div = num_one / num_two
print('Division:',ans_div)
ans_rem = num_two % num_one
print('Remainder:',ans_rem)
ans_exp = num_one ** num_two
print('Exponent:',ans_exp)
ans_flo = num_one // num_two
print('Floor Division:',ans_flo)

# calculate area and circumference of circle

radius = input('Enter Radius of the circle:')
pi = numpy.pi

area_circle = pi * (float(radius) ** float(2))
circumference_circle = float(2) * pi * float(radius)

print('Area of the Circle:', area_circle)
print('Circumference of the Circle:', circumference_circle)
