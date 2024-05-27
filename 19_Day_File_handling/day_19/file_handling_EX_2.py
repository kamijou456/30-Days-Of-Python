import os
import sys
import json
import xml
import xlrd
import re
import csv 


email_file_path = r'C:\Users\tylorxe\Documents\code_projects\Python\30-Days-Of-Python\data\email_exchanges_big.txt'

# 4

email_open = open(email_file_path)

email = email_open.read()

incoming_email_address = re.findall(r'From: .+' , email)

email_lst = []

[email_lst.append(re.sub('From: ' , '' , i , re.I)) for i in incoming_email_address]

dup_remove_lst = []

[dup_remove_lst.append(i) for i in email_lst if i not in dup_remove_lst]

dup_remove_lst.sort()

print(dup_remove_lst)

email_open.close()

obama_speech = r'C:\Users\tylorxe\Documents\code_projects\Python\30-Days-Of-Python\data\obama_speech.txt'

michelle_speech = r'C:\Users\tylorxe\Documents\code_projects\Python\30-Days-Of-Python\data\michelle_obama_speech.txt'

trump_speech = r'C:\Users\tylorxe\Documents\code_projects\Python\30-Days-Of-Python\data\donald_speech.txt'

melina_speech = r'C:\Users\tylorxe\Documents\code_projects\Python\30-Days-Of-Python\data\melina_trump_speech.txt'

# 5 and 6

def find_most_common_words(text:str , numoflst:int):

    if 'C:' in text:

        text_open = open(text)

        text_read = text_open.read()

    else:

        text_read = text

    word_lst = re.findall(r'\w+' , text_read)

    most_used_words = []

    [most_used_words.append((word_lst.count(i) , i)) for i in word_lst if (word_lst.count(i) , i) not in most_used_words]

    most_used_words.sort(reverse=True)

    text_open.close()

    return most_used_words[0:numoflst]

print(find_most_common_words(obama_speech,10))

print(find_most_common_words(michelle_speech,3))

print(find_most_common_words(trump_speech,3))

print(find_most_common_words(melina_speech,3))

romeo_juliet = r'C:\Users\tylorxe\Documents\code_projects\Python\30-Days-Of-Python\data\romeo_and_juliet.txt'

# print(find_most_common_words(romeo_juliet,10))

# 9

hacker_csv_open = open(r'C:\Users\tylorxe\Documents\code_projects\Python\30-Days-Of-Python\data\hacker_news.csv')

hacker_csv_reader = csv.reader(hacker_csv_open , delimiter=',')

number_python = 0

number_javascript = 0

for row in hacker_csv_reader:

    if 'Python' or 'python' in row:

        number_python += 1
    
    if 'Javascript' or 'JavaScript' or 'javascript' in row:

        number_javascript += 1

print(number_python)

print(number_javascript)