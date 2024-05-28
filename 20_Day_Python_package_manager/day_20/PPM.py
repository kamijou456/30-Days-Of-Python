import requests
import os
import sys
import re

sys.path.insert(0 , os.environ['USERPROFILE'] + r'\Documents\code_projects\Python\30-Days-Of-Python\19_Day_File_handling\day_19')

from file_handling_EX_2 import find_most_common_words

rom_and_juls = 'https://www.gutenberg.org/files/1112/1112-0.txt'

romjuls_response = requests.get(rom_and_juls)

romjuls_text = romjuls_response.text

print(find_most_common_words(romjuls_text , 10))