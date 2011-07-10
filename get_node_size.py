#!/usr/bin/python
import sys
import codecs
import urllib
import random
import re

f = codecs.open('stars', encoding='utf-8')
names = []
for name in f:
  if name[-1] == '\n':
    name = name[:-1]
  names.append(name)
f.close()

list_length = len(names)

f = open('hotness', 'a')

for name in names:
    query_str=urllib.urlencode({'': name.encode('UTF-8')})[1:]
    url_address = "http://www.baidu.com/s?wd="+query_str+"&inputT=%d"%random.randint(1, 1000)
    print url_address

    total = 0
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
    f.write(str(float(total)/10000)+'\n')
    f.flush()

f.close()
