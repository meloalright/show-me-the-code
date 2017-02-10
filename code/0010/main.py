#main.py
'''
第 0010 题：使用 Python 生成类似于下图中的字母验证码图片
'''

import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
from create_code import cr_200_code

def create_background():
    data = np.zeros((128,512,3), dtype=np.uint8)


    for i in range(len(data)):
        for j in range(len(data[i])):
            #for color_index in range(3):
                #data[i][j][color_index] =  random.choice(random_array)
            data[i][j][0] =  188
            data[i][j][1] =  188
            data[i][j][2] =  188

    img = Image.fromarray(data, 'RGB')
    return img

def add_noise(im):
    data = np.array(im)
    random_array = list(range(0,256))

    for i in range(len(data)):
        for j in range(len(data[i])):
            for color_index in range(3):
                if random.random() > 0.6:
                    data[i][j][color_index] =  random.choice(random_array)

    img = Image.fromarray(data, 'RGB')
    return img

def add_code(im, code):
    l = len(code)
    size = im.size
    fontsize = int(size[0] / l)
    height = int(size[1])
    myfont = ImageFont.truetype('Arial.ttf', fontsize)
    for i in range(l):
        index = i + 0.25
        char = code[i]
        color = 'rgb(' + str(int(random.uniform(0, 256))) + ',' + str(int(random.uniform(0, 256))) + ',' + str(int(random.uniform(0, 256))) + ')'
        ImageDraw.Draw(im).text((index * fontsize, (height-fontsize) / 2), char, font=myfont, fill = color)
    return im

'''
run
'''
bg = create_background()
code = cr_200_code()[123]
verify = add_code(bg, code)
noise_img = add_noise(verify)
#noise_img = (verify)
noise_img.show()