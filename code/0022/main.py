#main.py
from PIL import Image

from A import func
'''
相对引用引入A.func.resize.resize
'''


print(func.resize.resize)

im = Image.open('./img/photo.jpg')


'''
iphone6plus的宽高
'''
iphone_width = 828
iphone_height = 1472

func.resize.Image = Image

dist = func.resize.resize(im, iphone_width, iphone_height)#重定图片大小
dist.show()