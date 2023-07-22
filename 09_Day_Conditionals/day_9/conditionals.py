# exercise 1

driver_age = int(input('Enter Your Age: '))

if driver_age >= 18:
    print('You are old enough to get a drivers license.')
else:
    print('You need to wait', 18 - driver_age, 'more years before you can get a license.')

# exercise 2
q_age = int(input('Enter Your Age: '))
my_age = 29
ch_age = 'years'

if q_age < my_age:
    if my_age - q_age == 1:
        ch_age = 'year'
    print('You are', my_age - q_age, ch_age, 'younger than me.')
elif q_age > my_age:
    if q_age - my_age == 1:
        ch_age = 'year'
    print('You are', q_age - my_age, ch_age, 'older than me.')
else:
    print('We are the same age!')

# exercise 3

nOne = input('Enter First Number: ')
nTwo = input('Enter Second Number: ')

if nOne > nTwo:
    print(nOne, 'is greater than', nTwo)
elif nOne < nTwo:
    print(nOne, 'is less than', nTwo)
else:
    print(nOne,'and', nTwo, 'have the same value')

# exercise 4
student_dic = {}
number_students = int(input('Enter Number of Students in Your Class: '))

print('Enter the Students name followed by their assignment score.')

while len(student_dic) < number_students:
    student_name = input('Enter Students name: ')
    student_score = int(input('Enter Students score: '))
    if student_score >= 90:
        student_grade = 'A'
    elif student_score >= 80 and student_score <= 89:
        student_grade = 'B'
    elif student_score >= 70 and student_score <= 79:
        student_grade = 'C'
    elif student_score >= 60 and student_score <= 69:
        student_grade = 'D'
    else:
        student_grade = 'F'
    student_dic[student_name] = student_grade

print(student_dic)

# exercise 5

autumn = ['september', 'october', 'november']
winter = ['december', 'january', 'february']
spring = ['march', 'april', 'may']
summer = ['june', 'july', 'august']

input_month = input('Enter a month: ').lower()


if input_month in autumn:
    print('the season is Autumn')
elif input_month in winter:
    print('the season is Winter')
elif input_month in spring:
    print('the season is Spring')
elif input_month in summer:
    print('the season is Summer')
else:
    print('invalid entry please start over')



# exercise 6

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_input = input('Enter a Fruit to the grocery list: ').lower()

if fruit_input in fruits:
    print('Fruit is already on the list.')
else:
    fruits.append(fruit_input)
    print('Fruit has been added to the list!')
    print(fruits)


# exercise 7

Fname = input('Enter first name: ')
Lname = input('Enter last name: ')
Age = input('Enter age: ')
Country = input('Enter Country: ')
Is_married = False
Skills = ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
Address = input('Enter address: ')

person ={'first_name':Fname, 'last_name':Lname, 'age':Age, 'country':Country, 'is_married':Is_married, 'skills':Skills, 'address':Address}

if 'skills' in person:
    print(person['skills'][2])
    if 'skills' in person and 'Python' in person['skills']:
        print('Person has python experience!')

if person['is_married'] == Is_married and Country in person['country']:
    print(person['first_name'],person['last_name'], 'lives in', person['country'], 'He is not Married')
