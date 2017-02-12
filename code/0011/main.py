#main.py
import os
import re

words = open('./filtered_words.txt').read().split('\n')

input_str = input("请输入文字: ")


def search_filtered_word():
    for word in words:
        reg = re.compile(word)
        if reg.search(input_str):
            return True

    return False

f = search_filtered_word()
if f:
    print('Freedom')
else:
    print('Human Rights')