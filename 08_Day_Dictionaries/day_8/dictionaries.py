# Adding items to dictionary
dog = {}

dog['name'] = 'maxine'
dog['color'] = 'blond'
dog['breed'] = 'goldendoodle'
dog['legs'] = 4
dog['age'] = 1
print(dog)

# Creating student dictionary

firstName = input('First Name: ')
lastName = input('Last Name: ')
gender = input('Gender: ')
age = input('Age: ')
maritalStatus = input('Marital Status: ')
skills = [input('Enter First Skill: '), input('Enter Second Skill: '), input('Enter Third Skill: '), input('Enter Fourth Skill: ')]
country = input('Country: ')
city = input('City: ')
address = input('Address: ')

students = {'first_name':firstName, 'last_name':lastName, 'gender':gender, 'age':age, 'marital_status':maritalStatus, 'skills':skills, 'country':country, 'city':city, 'address':address}

print(students)

print(len(students))

print(students['skills'])

print(type(students['skills']))

students['skills'] = skills + [input('Enter Another Skill: '), input('And Another One: ')]

print(students.keys())

print(students.values())

print(students.items())

print(students)

students.popitem()

students.pop('marital_status')

del students['gender']

print(students)

del dog