import sys
import os

sys.path.insert(0, os.environ['USERPROFILE'] + '\\Documents\\code_projects\\Python\\30-Days-Of-Python\\data')

from countries import countries
from countries_data import country_info

# exercise level 1

# 1

numbers = [0,1,2,3,4,5,6,7,8,9,10]
numbers_count = 0

for n in numbers:
    print(n)

while numbers_count <= 10:
    print(numbers_count)
    numbers_count = numbers_count + 1

# 2
num = [10,9,8,7,6,5,4,3,2,1,0]
num_count = 10

for i in num:
    print(i)

while num_count >= 0:
    print(num_count)
    num_count = num_count - 1

# 3 and 4

triangle = '#'
triangle_lst = []

while len(triangle_lst) <= 7:
    while len(triangle) <= 7:
        print(triangle)
        triangle += '#'
    triangle_lst.append(triangle)

for it in triangle_lst:
    print(it)

# 5

count = 0
count_ans = 0

while count_ans < 100:
    count_ans = count * count
    print(count, 'X', count, '=', count_ans)
    count += 1

# 6

skill_lst = ['python', 'numpy', 'pandas', 'django', 'flask']

for skill in skill_lst:
    print(skill)

# 7

for number in range(0,101,2):
    print(number)

# 8

for nums in range(1,101,2):
    print(nums)

# exercise level 2 

# 1

print('sum of range is :', sum(range(0,101)))

# 2

print('sum of even numbers in range:', sum(range(0,101,2)), 'and sum of odd numbers in range:', sum(range(1,101,2)))

# exercise level 3 

# 1

print('\n \ncountries with land in their name:\n')

for country in countries:
    if 'land' in country:
        print(country)

# 2

fruit = ['banana', 'orange', 'mango', 'lemon']
new_fruits = ['banana', 'orange', 'mango', 'lemon']

for fruits in fruit:
    if fruits == 'banana':
        new_fruits[3] = fruits
    elif fruits == 'orange':
        new_fruits[2] = fruits
    elif fruits == 'mango':
        new_fruits[1] = fruits
    elif fruits == 'lemon':
        new_fruits[0] = fruits
    else:
        print('fruit list does not have any valid items')

print(new_fruits)

# 3

spoken_lang = []
dub_spoken_lang = []
lang_dct = {}
pop_dct = {}

for country in country_info:
    for lang in country['languages']:
        if lang in spoken_lang:
            continue
        else:
            spoken_lang.append(lang)
    dub_spoken_lang += country['languages']

    pop_dct[country['name']] = country['population']

for language in spoken_lang:
    lang_dct[language] = dub_spoken_lang.count(language)

print('Total number of different languages:', len(spoken_lang))

top10_lan = sorted(lang_dct.items(), key=lambda x:x[1], reverse=True)

print('Top ten most spoken languages:')

for lan in top10_lan[:10]:
    print(lan)

top10_pop = sorted(pop_dct.items(), key=lambda x:x[1], reverse=True)

print('Top Ten populated countries:')

for pop in top10_pop[:10]:
    print(pop)

# 6495