#main.py
import os

html = open('./file/file.html')

def get_paragraph(html):
    paragraph = []
    lines = html.readlines()
    for line in lines:
        line = line.strip()
        if line.startswith('<p>'):
            paragraph.append(line)
    return paragraph


paragraph = get_paragraph(html)
for p in paragraph:
    print(p + '\n')