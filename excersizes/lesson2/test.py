#!/usr/bin/python3
#encoding: utf-8
import random

text = "Ada!!!!!bsd,fsda?bsd bsd Bsd zsdasd:xsdqwe-qsdzzz"
test = "Asda!!!!!bsd,fsda?bsd bsd Bsd zsdasd:xsdqwe-qsdzzz"
split = ["!",".","?",",",":","-"]
	

for x in split:
	test = test.replace(x," ")
	test = test.lower()
test = test.split()
a = random.choice(test) 
words = set(test)
dic = dict.fromkeys(words,0)

for x in test:
	if x in dic.keys():
		dic[x] +=1



#a = dic.keys()
print dic
#print test
#print sorted(dic.items(), key = lambda x : x[0])[:3]