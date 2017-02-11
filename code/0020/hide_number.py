#hide_number.py
import json
from lxml import etree
from xlwt import Workbook
import xlrd, codecs

excel = xlrd.open_workbook("./unicom.xls");
sheet = excel.sheet_by_name("2017年02月语音通信");

excel_editing = Workbook()
sheet_editing = excel_editing.add_sheet('2017年02月语音通信')
'''
隐藏电话号码一部分数字 => 对2-7位隐藏
'''
for i in range(sheet.nrows):
    row = sheet_editing.row(i)
    for j in range(sheet.ncols):
        if i > 0 and j == 5:
            st = str(sheet.cell(i, j).value)
            new_st = '1' + '******' + st[7:]
            row.write(j, new_st)
        else:
            row.write(j, str(sheet.cell(i, j).value))

excel_editing.save('unicom.xls')
