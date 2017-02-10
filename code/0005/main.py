#main.py
import os
from PIL import Image

'''
引入该文件夹全部图片
'''
dirs = os.listdir('./img/')

'''
iphone5的宽高
'''
iphone_width = 640
iphone_height = 1136

'''
 重置图片大小函数
 @img 图片文件
 @iw 限制宽度
 @ih 限制高度
'''
def resize(img, iw, ih):
    w, h = img.size
    w_ratio = w/iw
    h_ratio = h/ih
    if w_ratio > 1 and w_ratio > h_ratio:
        ratio = w_ratio
    elif h_ratio > 1 and h_ratio > w_ratio:
        ratio = h_ratio
    else:
        ratio = 1
    return img.resize(
        (int(w / ratio), int(h / ratio))
        , Image.ANTIALIAS)

for imstr in dirs:
    im = Image.open('./img/' + imstr)#打开图片
    dist = resize(im, iphone_width, iphone_height)#重定图片大小
    dist.save('./dist/' + imstr)#保存