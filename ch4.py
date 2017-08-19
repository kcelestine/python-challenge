#!/usr/bin/python

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
