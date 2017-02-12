#
import json
from xlwt import Workbook

str = open('./numbers.txt').read()
data = json.loads(str)

'''
turn
'''
excel = Workbook()
sheet1 = excel.add_sheet('numbers')

'''
[
    [1, 82, 65535],
    [20, 90, 13],
    [26, 809, 1024]
]
'''

for i in range(len(data)):
    index = i
    row = sheet1.row(index)
    for j in range(len(data[i])):
        row.write(j, data[i][j])

excel.save('numbers.xls')
