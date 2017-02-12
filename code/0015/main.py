#
import json
from xlwt import Workbook

str = open('./city.txt').read()
data = json.loads(str)

'''
turn
'''
excel = Workbook()
sheet1 = excel.add_sheet('city')

'''
{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
'''

for i in data:
    index = int(i) - 1
    row = sheet1.row(index)
    row.write(0, data[i])

excel.save('city.xls')
