#main.py
import json
from lxml import etree
import xlrd, codecs

tree = etree.ElementTree(etree.Element("xml-tree"));

excel = xlrd.open_workbook("./city.xls");
sheet = excel.sheet_by_name("city");


for row in range(sheet.nrows):
    attr = {}

    for col in range(0, sheet.ncols):
        if sheet.cell(row, col).value != None and type(sheet.cell(row, col).value) == str:
            attr[row] = sheet.cell(row, col).value

    #print(attr)
    sub = etree.SubElement(tree.getroot(), "city")
    sub.text = json.dumps(attr, ensure_ascii=False)

etree.dump(tree.getroot())

ouput = codecs.open('./city.xml', 'w', 'utf-8');
ouput.write(etree.tounicode(tree.getroot()))
ouput.close()