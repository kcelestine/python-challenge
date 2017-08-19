#!/usr/bin/python

import re

f = open('4_help', 'r')
lines = f.readlines()

count = 0
def check(text):
	pattern="([A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z])"
	if re.search(pattern,  text):
		return True
	else:
		return False

for line in lines:
	if(check(line)):
		print line

