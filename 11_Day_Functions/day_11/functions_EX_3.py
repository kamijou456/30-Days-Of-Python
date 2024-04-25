# 1

num = 20

prime_num = 17

num_lst = [20,17]

def is_prime(i):

    if type(i) == int and i % 2 != 0:

        print("Number is Prime")

    elif type(i) == int and i % 2 == 0:

        print("Number is not Prime")

    else:

        print("Incorrect input data type")

is_prime(num)

is_prime(prime_num)

is_prime(num_lst)

# 2

evn_num_lst = [1,2,3,4,5,6,7,8,9,10]

odd_num_lst = [2,15,6,11,13,8,5]

rep_num_lst = [5,5,5,3,3,3,3,3,3,3,3,3,3,4,4,4,4,10,10,9,13,13,13,13,13,13,13,13,13,13]

str_num_lst = ["h",1,3,4,"o",5,6,"w"]

def check_unique(lst):

    uni_lst = []

    for i in lst:

        count = lst.count(i)

        if count > 1:

            non_uni = "Item " + str(i) + " in the list is not unique and is repeated " + str(count) + " times."

            uni_lst.append(non_uni)

        else:

            uni = "Item " + str(i) + " in the list is unique"

            uni_lst.append(uni)

    for i in uni_lst:

        count = uni_lst.count(i)

        while count > 1:

            count = uni_lst.count(i)

            uni_lst.remove(i)

        print(i)

check_unique(rep_num_lst)

check_unique(evn_num_lst)

check_unique(odd_num_lst)

# 3

def check_samevari(lst):

    vari_lst = []

    for i in lst:

        vari_type = type(i)

        vari_lst.append(vari_type)

    check_output = vari_lst.count(vari_lst[0]) == len(vari_lst)

    return check_output

print("Checking if all items in a list are of the same data type: " , check_samevari(rep_num_lst))

print("Checking if all items in a list are of the same data type: " , check_samevari(str_num_lst))

# 4

test_str = "hello"

test_str2 = "2hello"

test_str3 = "hello world"

test_str4 = "hello_world"

def test_vari(var):

    if var.isidentifier():

        print("string can be used as a valid variable")

    else:

        print("string cannot be a valid variable")

test_vari(test_str)

test_vari(test_str2)

test_vari(test_str3)

test_vari(test_str4)

# 5

import sys
import os

sys.path.append(os.environ['USERPROFILE'] + '\\Documents\\code_Projects\\Python\\30-Days-Of-Python\\data')

from countries_data import country_info

def top_languages(lst):

    lang_count = []

    lang_filter = []

    for i in lst:

        lang = i.get("languages")

        for i in lang:

            lang_count.append(i)

    for i in lang_count:

        count = lang_count.count(i)

        count_tpl = (count,i)

        lang_filter.append(count_tpl)

    for i in lang_filter:

        spec_lang_count = lang_filter.count(i)

        while spec_lang_count > 2:

            spec_lang_count = lang_filter.count(i)

            lang_filter.remove(i)

    
    lang_filter.sort()

    for i in range(-1,-21,-1):

        print(lang_filter[i])

top_languages(country_info)

# 6

def most_populated_countries(lst):

    pop_filter = []

    for i in lst:

        country_name = i.get("name")

        pop = i.get("population")

        pop_tpl = (pop,country_name)

        pop_filter.append(pop_tpl)

    pop_filter.sort()

    for i in range(-1,-21,-1):

        print(pop_filter[i])

most_populated_countries(country_info)