#
import json
from xlwt import Workbook

str = open('./student.txt').read()
data = json.loads(str)

'''
turn
'''
excel = Workbook()
sheet1 = excel.add_sheet('student')

'''
data = {
    "1":["张三",150,120,100],
    "2":["李四",90,99,95],
    "3":["王五",60,66,68]
}
'''

for i in data:
    index = int(i) - 1
    row = sheet1.row(index)
    for j in range(len(data[i])):
        row.write(j, data[i][j])

excel.save('student.xls')