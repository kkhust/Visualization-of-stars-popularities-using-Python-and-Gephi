import codecs

# read the names
names = []
f = codecs.open('stars', 'r', encoding='utf-8')
for name in f:
	if name[-1] == '\n':
		name = name[:-1]
	names.append(name)
f.close()

# read the scores
scores = []
f = open('res.txt', 'r')
for line in f:
	scores.append(int(line))
f.close()

# read the gender
gender = []
f = open('gender', 'r')
for line in f:
	gender.append(int(line))
f.close()

# create the node
f = codecs.open('stars.graphml', 'w', encoding='utf-8')
for i, name in enumerate(names):
	f.write("<node id='%s'>\n" % name)
	f.write("<data key='d0'>%d</data>\n" % gender[i])
	f.write("<data key='d2'>%.1f</data>\n" % 0.0)
	f.write("</node>")

def get_relations(scores, num, idx):
	res = []
	def get_pos (n): return lambda x,y: (2*n-1-y)*y/2+(x-y)-1
	f = get_pos(num)
	for i in xrange(num):
		if i == idx:
			res.append(0)
		elif i < idx:
			res.append(scores[f(idx, i)])
		else:
			res.append(scores[f(i, idx)])
	return res

# create the edge
loc = 0
for i, name in enumerate(names):
	relations = get_relations(scores, len(names), i)
	assert(len(relations) == len(names))
	tmp = relations[:]; tmp.sort()
	threshold = 0
	for k in xrange(-1, -6, -1):
		if tmp[k] <= 0:
			break
		threshold = tmp[k]
	if threshold <= 0:
		continue
	count = 0
	for j in xrange(len(names)):
		if i == j:
			pass
		if relations[j]/threshold >= 1:
			f.write("<edge id='e%d' source='%s' target='%s'>\n" % (loc, name, names[j]))
			f.write("<data key='d1'>%d</data>\n" % relations[j])
			f.write("</edge>\n")
			loc += 1
			count += 1
	#print count

# for i, name in enumerate(names):
# 	for j in xrange(i+1, len(names)):
# 		if scores[loc] > 0:
# 			if name == names[j]:
# 				print i
# 			# create an edge
# 			f.write("<edge id='e%d' source='%s' target='%s'>\n" % (loc, name, names[j]))
# 			f.write("<data key='d1'>%d</data>\n" % scores[loc])
# 			f.write("</edge>\n")
# 		loc += 1

f.close()
