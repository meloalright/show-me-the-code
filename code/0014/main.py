#
import json
from xlwt import Workbook

str = open('./student.txt').read()
data = json.loads(str)

'''
str = '{
    "1":["张三",150,120,100],
    "2":["李四",90,99,95],
    "3":["王五",60,66,68]
}'
data = json.dumps('')
'''
excel = Workbook()
sheet1 = excel.add_sheet('student')
'''
row0 = sheet1.row(0)
row0.write(0,'cc2')
row0.write(1,'cc2')

row1 = sheet1.row(1)
row1.write(0,'A2')
row1.write(1,'B2')

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