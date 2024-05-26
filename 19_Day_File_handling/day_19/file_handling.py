import os
import sys
import json
import csv
import xml
import xlrd
import re


def num_of_lines_and_words(text):

    op = open(text)

    opread = op.read()

    oplines = opread.splitlines()

    opwords = opread.split()

    print("number of lines in text document: " , len(oplines))

    print("number of words in text document: " , len(opwords))

print("a)")

num_of_lines_and_words(r"C:\Users\tylorxe\Documents\code_projects\Python\30-Days-Of-Python\data\obama_speech.txt")

print("b)")

num_of_lines_and_words(r'C:\Users\tylorxe\Documents\code_projects\Python\30-Days-Of-Python\data\michelle_obama_speech.txt')

print("c)")

num_of_lines_and_words(r'C:\Users\tylorxe\Documents\code_projects\Python\30-Days-Of-Python\data\donald_speech.txt')

print("d)")

num_of_lines_and_words(r'C:\Users\tylorxe\Documents\code_projects\Python\30-Days-Of-Python\data\melina_trump_speech.txt')

def most_spoken_lang(filename: str , topoflist: int):

    languages_lst = []

    top_lst = []

    countries_json = open(filename , 'r' , encoding='utf-8')

    countries_json_r = countries_json.read()

    countries_dct = json.loads(countries_json_r)

    [languages_lst.extend(i['languages']) for i in countries_dct]

    for i in languages_lst:

        lang_tup = (languages_lst.count(i) , i)

        if lang_tup not in top_lst:

            top_lst.append(lang_tup)

    top_lst.sort(reverse=True)

    return print(top_lst[0:topoflist])

most_spoken_lang(filename=r'C:\Users\tylorxe\Documents\code_projects\Python\30-Days-Of-Python\data\countries_data.json', topoflist= 3)

country_file = r'C:\Users\tylorxe\Documents\code_projects\Python\30-Days-Of-Python\data\countries_data.json'

def most_populated_countries(filename:str , topoflist:int): 

    pop_list = []

    countries_json = open(filename , 'r' , encoding='utf-8')

    countries_json_r = countries_json.read()

    countries_dct = json.loads(countries_json_r)

    [pop_list.append({'country' : i['name'] , 'population' : i['population']}) for i in countries_dct]

    def myfunc(e):
        return e['population']
    
    pop_list.sort(key= myfunc , reverse= True)

    return print(pop_list[0:topoflist])

most_populated_countries(filename= country_file , topoflist= 3)