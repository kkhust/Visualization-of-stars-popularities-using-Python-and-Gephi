#!/usr/bin/python
import sys
import codecs
import urllib
import random
import re

args = sys.argv[1:]
if len(args) != 3:
  print 'Wrong arguments!'
  sys.exit(1)
input_filename = args[0]
output_filename = args[1]
start_idx = int(args[2])

f = codecs.open(sys.argv[1], encoding='utf-8')
names = []
for name in f:
  if name[-1] == '\n':
    name = name[:-1]
  names.append(name)
f.close()

list_length = len(names)
if start_idx >= list_length:
  print 'Wrong start index!'
  sys.exit(1)

f = open(output_filename, 'a')

for i in xrange(start_idx, list_length):
  name1 = names[i]
  hits = []
  for j in xrange(i+1, list_length):
    name2 = names[j]
    query_str=urllib.urlencode({'': name1.encode('UTF-8')})[1:]+'+'+urllib.urlencode({'': name2.encode('UTF-8')})[1:]
    url_address = "http://www.baidu.com/s?wd="+query_str+"&inputT=%d"%random.randint(1, 1000)
    #print url_address

    total = -1
    try:
      html_source = urllib.urlopen(url_address)
      for line in html_source:
        m = re.search(u'\xd5\xd2\xb5\xbd\xcf\xe0\xb9\xd8\xbd\xe1\xb9\xfb\xd4\xbc([0-9,]+)\xb8\xf6', line)
        if m is None:
          pass
        else:
          total = int(m.group(1).replace(',', ''))
          break
    except:
      pass
    print total
    hits.append(total/10000)

  # write the results to the disk
  for n in hits:
    f.write(str(n)+'\n')
  f.flush()

f.close()
