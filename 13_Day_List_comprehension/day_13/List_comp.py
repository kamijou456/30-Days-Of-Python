import string
# 1

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

only_neg = [i for i in numbers if i <= 0]

print(only_neg)

# 2

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flat_lst = [num for frow in list_of_lists for srow in frow for num in srow]

print(flat_lst)

# 3

lst_tup = [(i , 1 , i , i**2 , i**3 , i**4 , i**5) for i in range(11)]

[print(i) for i in lst_tup]

# 4

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flat_countries = [list(count) for row in countries for count in row]

new_str =  [count for count in flat_countries]


print(new_str)