#!/usr/bin/python

import re

f = open('4_help', 'r')
lines = f.readlines()

d = dict()

for line in lines:
	line = list(line)
	for c in line:
		d[c] = d.get(c, 0) +1
values = []
for k,v in d.items():
	values.append(v)

values.sort()

for v in values:
	print v

print values
	
def check(pattern, text):
	if re.search(pattern,  text):
		return 'found a match!'
	else:
		return 'no match!'

word = "AAAbAAA"
word2 = "ababaA3"

pattern="([A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z])"

print check(pattern, word)
print check(pattern, word2)
'''
for each line
	build word
	if word is 7 chars
	print word
'''
