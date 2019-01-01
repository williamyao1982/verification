#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup

openFile = "verification.txt"
f = open(openFile,"r")
lines = f.readlines()
for line in lines:
    line = line.strip()
    #print(line)
    val = line.split(',')
    val1 = val[0]
    val2 = val[1]
    print "val1 = %s" % val1;
    print "val2 = %s" % val2;
    url = val2
    version = val1
    r = requests.get(url)
    html = r.content
    soup = BeautifulSoup(html, features='lxml')
    verName = soup.find_all('div', {'style': 'color: #B33A3B; border-left: 1px solid #FFFFFF;'})
    for i in verName:
        print(i.get_text())
        if version in i.get_text():
            print "%s is True" % val2
        else:
            print "%s is False" % val1
f.close()