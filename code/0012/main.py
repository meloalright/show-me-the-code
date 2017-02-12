#main.py
import os
import re

words = open('./filtered_words.txt').read().split('\n')

inputs = input("请输入文字: ")


def replace_filtered_word(input_str):
    for word in words:
        reg = re.compile(word)
        if reg.search(input_str):
            input_str = re.sub(reg, '**', input_str)

    return input_str

filtered_str = replace_filtered_word(inputs)
print(filtered_str)