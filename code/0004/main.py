#main.py
import re

myfile = open('english.txt', 'r')


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

dc = get_dict_rank(myfile)
for item in dc:
    print("%s: %s"% (item, dc[item]))