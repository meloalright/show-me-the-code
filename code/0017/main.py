#main.py
import json
from lxml import etree
import xlrd, codecs

tree = etree.ElementTree(etree.Element("xml-tree"));

excel = xlrd.open_workbook("./student.xls");
sheet = excel.sheet_by_name("student");


for row in range(sheet.nrows):
    attr = {}

    for col in range(sheet.ncols):
        if sheet.cell(row, col).value != None and type(sheet.cell(row, col).value) == float:
            attr[col] = str(int(sheet.cell(row, col).value))
        elif sheet.cell(row, col).value != None and type(sheet.cell(row, col).value) == str:
            attr[col] = sheet.cell(row, col).value

    sub = etree.SubElement(tree.getroot(), "student", name=sheet.cell(row, 0).value)
    sub.text = json.dumps(attr, ensure_ascii=False)

etree.dump(tree.getroot())

ouput = codecs.open('./student.xml', 'w', 'utf-8');
ouput.write(etree.tounicode(tree.getroot()))
ouput.close()