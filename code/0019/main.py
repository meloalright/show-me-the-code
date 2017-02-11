#main.py
import json
from lxml import etree
import xlrd, codecs

tree = etree.ElementTree(etree.Element("xml-tree"));

excel = xlrd.open_workbook("./numbers.xls");
sheet = excel.sheet_by_name("numbers");

arr = []

for row in range(sheet.nrows):
    arr.append([])
    for col in range(0, sheet.ncols):
        if sheet.cell(row, col).value != None and type(sheet.cell(row, col).value) == float:
            arr[row].append(int(sheet.cell(row, col).value))


##
root = etree.SubElement(tree.getroot(), "root")
root.text = json.dumps(arr, ensure_ascii=False)

etree.dump(tree.getroot())

ouput = codecs.open('./numbers.xml', 'w', 'utf-8');
ouput.write(etree.tounicode(tree.getroot()))
ouput.close()