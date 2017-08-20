#!/usr/bin/python

import re

f = open('4_help', 'r')
lines = f.readlines()

count = 0
def check(text):
	pattern="[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+"
	if re.search(pattern,  text):
		return True
	else:
		return False

for line in lines:
	if(check(line)):
		count += 1 
		print line
print count

