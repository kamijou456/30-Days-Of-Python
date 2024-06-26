# 1

def evens_and_odds(n):

    even_lst = []

    odd_lst = []

    for i in range(n + 1):
        
        if i % 2 == 0:
            
            even_lst.append(i)

        else:
            odd_lst.append(i)

    print("Number of Even numbers: ", len(even_lst))

    print("Number of Odd numbers: ", len(odd_lst))

evens_and_odds(100)

# 2

def factorial(n):

    total = 1

    for i in range(1 , n + 1):

        total *= i

    return total

print("Factorial of input: ", factorial(10))

# 3

def is_empty(i):

    if len(i) == 0:
        
        print("Object is empty")

    else:

        print("Object is not empty")

empty_lst = []

empty_str = ""

empty_dic = {}

lst = [1,2,3]

str = "Howdy"

dic = {1:"H" , 2:"O" , 3:"W"}

is_empty(empty_lst)

is_empty(lst)

is_empty(empty_str)

is_empty(str)

is_empty(empty_dic)

is_empty(dic)

# 4

evn_num_lst = [1,2,3,4,5,6,7,8,9,10]

odd_num_lst = [2,15,6,11,13,8,5]

rep_num_lst = [5,5,5,3,3,3,3,3,3,3,3,3,3,4,4,4,4,10,10,9,13,13,13,13,13,13,13,13,13,13]

'''

print(type(len(evn_num_lst)))

print(evn_num_lst[int((len(evn_num_lst) / 2) - 1)])

print(evn_num_lst[int(len(evn_num_lst) / 2)])

odd_num_lst.sort()

print(odd_num_lst)

'''

def calculate_mean(lst):

    total = 0

    for i in lst:

        total += i

    mean = total / len(lst)

    return mean

print("Mean of numbers in the list: " , calculate_mean(evn_num_lst))

print("Mean of numbers in the list: " , calculate_mean(odd_num_lst))

# 5

def calculate_median(lst):

    lst.sort()

    if len(lst) % 2 == 0:

        num = lst[int(len(lst) / 2)] + lst[int(len(lst) / 2) - 1]

        median = num / 2

    else:

        median = lst[int(len(lst) / 2)]

    return median

    

print("Median of numbers in the list: " , calculate_median(evn_num_lst))

print("Median of numbers in the list: " , calculate_median(odd_num_lst))

# 6

def calculate_mode(lst):

    lst.sort()

    dct_lst = []

    for i in range(lst[-1] + 1):

        num_num = lst.count(i)

        if num_num > 0:

            tpl = (num_num , i)

            dct_lst.append(tpl)

    print(dct_lst)

    dct_lst.sort()

    mode = dct_lst[-1]

    return mode
    
print("Mode is number: " , calculate_mode(rep_num_lst)[-1] , "\nThe number of times the number is repeated: " , calculate_mode(rep_num_lst)[-2])

# 7

def calculate_range(lst):

    lst.sort()

    if len(lst) > 1:

        range_total = lst[-1] - lst[0]

    else:

        print("Not enough numbers in the list to have a range.")

    return range_total

print("Range of numbers in the list: " , calculate_range(odd_num_lst))

# 8 

def calculate_variance(lst):

    mean = calculate_mean(lst)

    total = 0

    for i in lst:

        dif = i - mean

        dif_sq = dif ** 2

        total += dif_sq

    vari = total / (len(lst) - 1)

    return vari

print("Variance of list: " , calculate_variance(rep_num_lst))

print("Variance of list: " , calculate_variance(evn_num_lst))

print("Variance of list: " , calculate_variance(odd_num_lst))

# 9

def calculate_std(lst):

    vari = calculate_variance(lst)

    std = vari ** (1/2)

    return std

print("Standard Deviation of list: " , calculate_std(rep_num_lst))

print("Standard Deviation of list: " , calculate_std(evn_num_lst))

print("Standard Deviation of list: " , calculate_std(odd_num_lst))