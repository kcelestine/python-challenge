f = open('ch3_help', 'r')
lines = f.readlines()

d = dict()

for line in lines:
	line = list(line)
	for c in line:
		d[c] = d.get(c, 0) +1

print d


for k,v in d.items():
	print("{:<12} {:<12}".format(k, v))

'''
counts = dict()
for i in items:
  counts[i] = counts.get(i, 0) + 1
'''
