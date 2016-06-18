#!/usr/bin/python
#encoding:utf-8


__author__ = 'Daniil Orlovskiy'

import sys
import re
import os
import codecs


page = open('babynames_boys.html','r')
page_text = page.read()
extract_reg = re.compile(r'<td.*?>([^\S].*?)</td>', re.DOTALL)
res = extract_reg.findall(page_text)
years = ['2012','2010','2005','2000','1990']
# print page_text
# for x in range(1,21,7):
# 	print res[x].strip()
b = lambda x:res[x].strip()
names_dict = {res[a].strip():{c:b(a+years.index(c)+1) for c in years} for a in range(1,21,7)}
print  names_dict
user_choice = '2012'
for key, value in sorted(names_dict.items()):
	print key, sorted(value.keys())

