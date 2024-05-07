import string
# 1

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

only_neg = [i for i in numbers if i <= 0]

# print(only_neg)

# 2

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flat_lst = [num for frow in list_of_lists for srow in frow for num in srow]

# print(flat_lst)

# 3

lst_tup = [(i , 1 , i , i**2 , i**3 , i**4 , i**5) for i in range(11)]

# [print(i) for i in lst_tup]

# 4

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flat_countries = [list(count) for row in countries for count in row]

[count.insert(1 , count[0][0:3]) for count in flat_countries]

edited_lst = []

[edited_lst.append([strg.upper() for strg in count]) for count in flat_countries]

'''

edited_lst = []

for itm in flat_countries:

    lst = []

    for str in itm:

        lst.append(str.upper())

    edited_lst.append(lst)

'''

print(flat_countries)

print(edited_lst)

# 5

lst_dct_countries = [{"country":count[0] , "city":count[2]} for count in flat_countries]

print(lst_dct_countries)

# 6 

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

flat_names = [list(count) for row in names for count in row]

name_lst = []

[name_lst.append(name[0] + " " + name[1]) for name in flat_names]

print(name_lst)

# 7

slope = lambda x2 , y2 , x1, y1 : (y2 - y1) / (x2 - x1)

print(slope(3,5,1,4))

y_intercept = lambda x2 , y2, x1 , y1 : y1 - (slope(x2,y2,x1,y1) * x1)

print(y_intercept(3,5,1,4))