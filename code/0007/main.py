import os

'''
第 0007 题：
有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来.
'''

answer = {
    'all': 0,
    'code': 0,
    'empty': 0,
    'note': 0
    }

dirs = os.listdir('./codes/')


def read_all_codes(file_str_list):
    for file_str in file_str_list:
        file = open('./codes/' + file_str)
        '''
        file.readlines()方法
        把文件的每一行代码存入list并返回
        '''
        codes_lines = file.readlines()

        #if_noting 判断是否为多行注释态
        if_noting = False

        for line in codes_lines:
            '''
            去除开头的空格
            '''
            line = line.strip()

            if(if_noting == True):
                '''
                处于多行注释态
                '''
                if line.startswith("'''"):
                    '''
                    多行注释态终结
                    '''
                    if_noting = False

                answer['note'] += 1
            else:
                '''
                不处于多行注释态
                '''
                if line.startswith("'''"):
                    #进入多行注释态
                    if_noting = True
                    answer['note'] += 1

                elif line.startswith("#"):
                    answer['note'] += 1

                elif line == '':
                    answer['empty'] += 1

                else:
                    answer['code'] += 1



    answer['all'] = answer['code'] + answer['empty'] + answer['note']
'''
call thi func
'''
read_all_codes(dirs)

#打印答案
print(answer)