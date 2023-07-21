# exercise 1
'''
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
'''
# exercise 4
student_dic = {}
number_students = int(input('Enter Number of Students in Your Class: '))

while len(student_dic) < number_students:
    print('Enter the Students name followed by their assignment score.')
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
