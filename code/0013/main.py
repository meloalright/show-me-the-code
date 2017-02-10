#main.py
import urllib.request
import urllib.parse
import re
from os.path import basename

url = "http://huaban.com/search/?q=%E9%83%AD%E9%9B%AA%E8%8A%99"

def getPage(url):
    #url = url
    #urlContent = urllib.request.urlopen(url).read()
    #page = '<span class="red">(.*?)</span>'
    #thePage=re.findall(page,urlContent)
    #return int(thePage[0])
    return 5

def downImg(url):
    urlContent = str(urllib.request.urlopen(url).read())
    reg = re.compile('img .*?src="(.*?)"')
    '''
    (.*?)括号内的数据作为结果返回例如
    '''
    imgUrls = re.findall(reg, urlContent)
    for imgUrl in imgUrls:
        try:
            imgData = urllib.request.urlopen('http:' + imgUrl).read()
            fileName = basename(urllib.parse.urlsplit(imgUrl)[2])
            output = open('./download/' + fileName + '.jpg','wb')
            output.write(imgData)
            output.close()
        except:
            print("Er..")

def downLoad(url):
    #numb = getPage(url)
    #cont = 0
    downImg(url)
    print('Completed!')

downLoad(url)