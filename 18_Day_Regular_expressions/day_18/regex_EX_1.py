import re

paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."

def lst_of_mostusedwords(str):

    lst = []

    lst_of_words = re.findall(r'\w+', str)

    [lst.append((lst_of_words.count(i), i)) for i in lst_of_words if (lst_of_words.count(i), i) not in lst]

    lst.sort(reverse=True)

    return lst

print(lst_of_mostusedwords(paragraph))

# 2

str_example = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles."


def len_of_range(str):

    joined_lst = re.findall(r'-\d+', str) + re.findall(r' \d+', str)

    int_lst = []

    [int_lst.append(int(i)) for i in joined_lst]

    int_lst.sort()

    len_of_range = int_lst[-1] - int_lst[0]

    return len_of_range

print(len_of_range(str_example))

# 3

def is_valid_variable(strg):
    return print(strg.isidentifier())

is_valid_variable("first_name")

is_valid_variable('first-name')

is_valid_variable('1first_name')

is_valid_variable('firstname')

# 4

sentence = "%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?"

clean_sentence = re.sub("[^A-Za-z ]", "", sentence)

print(clean_sentence)

print(lst_of_mostusedwords(clean_sentence)[0:3])