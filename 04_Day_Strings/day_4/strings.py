# Learning to manipulate string data types in python
# EX 1
string1 = 'Thirty ' + 'Days ' + 'Of ' + 'Python'
print(string1)
# EX 2,3,4,5
company = 'Coding ' + 'For ' + 'All'
print(company)
print(len(company))
# EX 6,7,8
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
# EX 9
print(company.replace('Coding ', ''))
# EX 10
print(company.find('Coding'))
# EX 11
print(company.replace('Coding ', 'Python '))
# EX 12 
string2 = 'Python For Everyone'
print(string2.replace('Everyone', 'All'))
# EX 13
print(company.split())
# EX 14
string3 = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(string3.split(', '))
# EX 15 
print(company[0])
# EX 16
last_index = len(company) - 1
print(last_index)
# EX 17
print(company[10]) # its a space
# EX 18, 19
print(string2[0], string2[7], string2[11])
print(company[0], company[7], company[11])
# EX 20, 21
print(company.index('C'))
print(company.index('F'))
# EX 22
string4 = 'Coding For All People'
print(string4.rfind('l'))
# EX 23, 24, 25 ,26, 27
string5 = 'You cannot end a sentence with because because because is a conjunction'
print(string5.index('because'))
print(string5.rindex('because'))
print(string5.replace('because because because ', ''))
# EX 28, 29
print(company.startswith('Coding'))
print(company.endswith('Coding'))
# EX 30
string6 = '  Coding For All  '
print(string6.strip(' '))
# EX 31
string7 = '30DaysOfPython'
string8 = 'thirty_days_of_python'
print(string7, string7.isidentifier(), ': ', string8, string8.isidentifier())
# EX 32
string9 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
string10 = '# '.join(string9)
print(string10)
# EX 33, 34
string11 = 'I am enjoying this challenge.\nI just wonder what is next.'
print(string11)
string12 = 'Name\tAge\tCountry\tCity\nJJ\t29\tUSA\tFort Worth'
print(string12)
# EX 35
string13 = 'radius = 10\narea = 3.14 * radius ** 2\nThe area of a circle with radius 10 is 314 meters square.'
print(string13)
# EX 36
string14 = '''8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144'''
print(string14)