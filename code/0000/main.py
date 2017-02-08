#main.py
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

def add_redot(imgfile, num):
    im = Image.open(imgfile)
    size = im.size
    fontsize = int(size[1]/8)
    myfont = ImageFont.truetype('Arial.ttf', fontsize)
    ImageDraw.Draw(im).text((7.5 * fontsize, 0.5 * fontsize), str(num), font=myfont, fill = 'red')
    plt.imshow(im)
    plt.title('redot')
    plt.show()




#run here
add_redot('photo.jpg', 2)