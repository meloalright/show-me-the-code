#main.py
import json
from lxml import etree
from xlwt import Workbook
import xlrd, codecs

excel = xlrd.open_workbook("./unicom.xls");
sheet = excel.sheet_by_name("2017年02月语音通信");

'''
'''

whole = 0

for i in range(sheet.nrows):
    #row = sheet.row(i)
    for j in range(sheet.ncols):
        if i > 0 and j == 3:
            strr = str(sheet.cell(i, j).value)
            msplit = strr.split('分')
            try:
                secondstr = msplit[1]
                minute = int(msplit[0])
            except:
                minute = 0
                secondstr = msplit[0]
            ssplit = secondstr.split('秒')
            seconds = int(ssplit[0])

            #通话时间
            period = minute * 60 + seconds
            print('%s\'%s\" == %s\''%(minute, seconds, period))
            whole += period
        else:
            pass

print('总共 => %s秒'%whole)
