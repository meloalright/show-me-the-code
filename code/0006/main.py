#main.py
import os
import re

dirs = os.listdir('./dairy/')


def get_dict_rank(txt):
    words = re.findall(r"[\w']+", txt.read())
    '''
    re.findall => 匹配正则表达式并返回一个list
    r"[\w']+" => 匹配英文
    '''

    dictionary = {}

    for word in words:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    return dictionary

'''
排除日常常用介词的干扰
'''
regular_vocabulary = ['and', 'else', 'then', 'that', 'the', 'this', 'or' ,'with', 'of', 'a', 'are', 'as', 'some']

def get_top(dictionary):
    top = ''
    max = 0
    '''
    如果这个词出现率[比前面的都高]+而且还不属于日常介词:
        就放到top里
    如果这个词出现率[和最高的一样高]+而且还不属于日常介词:
        和top并列
    '''
    for i in dictionary:
        if dictionary[i] > max and i not in regular_vocabulary:
            top = i
            max = dictionary[i]
        elif dictionary[i] == max and i not in regular_vocabulary:
            top = top + ' ' + i
    return top


for dairy_name in dirs:
    dairy = open('./dairy/' + dairy_name, 'r')
    dc = get_dict_rank(dairy)
    top = get_top(dc)
    print('%s: %s' % (dairy_name, top))