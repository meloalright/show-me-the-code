#main.py
import os
import re



html = open('./file/file.html')

pattern = re.compile(r'href=\S+"')

def get_links(html):
    links = []
    lines = html.readlines()
    for line in lines:
        line = line.strip()
        if line.startswith('<a') and pattern.search(line):
            if pattern.search(line).group().split('href="')[1].startswith('javascript:'):
                pass
            else:
                links.append(line)
    return links


links = get_links(html)
for link in links:
    print(link + '\n')