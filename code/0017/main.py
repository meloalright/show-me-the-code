#main.py
import json
from lxml import etree
import xlrd, codecs

tree = etree.ElementTree(etree.Element("xml-tree"));

excel = xlrd.open_workbook("./student.xls");
sheet = excel.sheet_by_name("student");

attr = {}

for row in range(sheet.nrows):

    for col in range(1, sheet.ncols):
        if sheet.cell(row, col).value != None and type(sheet.cell(row, col).value) == float:
            attr[col] = str(int(sheet.cell(row, col).value))
        if sheet.cell(row, col).value != None and type(sheet.cell(row, col).value) == str:
            attr[col] = sheet.cell(row, col).value

    #print(attr)
    sub = etree.SubElement(tree.getroot(), "student", name=sheet.cell(row, 0).value)
    sub.text = json.dumps(attr)

etree.dump(tree.getroot())

ouput = codecs.open('./student.xml', 'w', 'utf-8');
ouput.write(etree.tounicode(tree.getroot()))
ouput.close()