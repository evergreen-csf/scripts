#! /usr/local/bin/python
import fileinput
import re

DATA_DIR = "/home/localbox/src/csf-data"

f = open(DATA_DIR+'/blah.txt', 'a')

p = re.compile('Subject: Fw: ([\w]+) added you to ([\w]+)')
#p = re.compile('From: [\w,\s]+ \[([\w,\s,@,<,>,.,-]+)\]')
#p = re.compile('On ([\w,\s,\,,:]+), ([\w,\s,@,<,>,.,-]+) wrote:')

for line in fileinput.input():
	m = p.match(line)
#	f.write(line)
	if (m != None):
		sender = m.group(1)
		repo = m.group(2)
		f.write(sender+" "+repo+"\n")

f.close()
