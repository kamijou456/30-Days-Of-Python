# Day 5 Praticing Lists
empty_list = []

six_items = ['one','two','three','four','five','six']

first, second, third, fourth, fifth, sixth = six_items

print('First List:', len(empty_list), 'Second List:', len(six_items))

print(first, third, sixth)

mixed_data_types =['JJ', 29, 6.1, True, '4000 Golding Ave']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print('Number of companies:', len(it_companies))
print(it_companies[0], it_companies[int(len(it_companies)/2)], it_companies[len(it_companies)-1])

it_companies[len(it_companies)-1] = 'Gooberzon'
print(it_companies)

it_companies.append('Twitter')

it_companies.insert(4,'Meta')

it_companies[2] = it_companies[2].upper()

string1 = ['#;  ']

join1 = it_companies + string1

print(join1)

#company = input('Enter Tech Company to verify if it is on the list: ')

#company = company.capitalize()

#it_companies_find = it_companies.__contains__(company)

#print('Result:', it_companies_find)


print(sorted(it_companies))

print(sorted(it_companies,reverse=True))

print(it_companies[2:])

print(it_companies[:-3])

print(it_companies[0:3] + it_companies[4:])

print(it_companies)

it_companies.pop(0)
print(it_companies)
it_companies.pop(3)
print(it_companies)
it_companies.pop()
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end

full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)