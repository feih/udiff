#!/usr/bin/python

import sys

if len(sys.argv) == 1:
    print
    print "Usage: urlDiff.py firstHTTPURL secondHTTPURL"
    print "Output: base - firstHTTPURL"
    print "        comp - secondHTTPURL"
    print
    sys.exit(0)

baseline = sys.argv[1]
compare  = sys.argv[2]

#print baseline
#print compare

baseline = baseline.split('?')[1]
compare = compare.split('?')[1]

base_split = baseline.split('&')
comp_split = compare.split('&')

D = dict()

def store(splitted, isBase):

    for kv  in splitted:
	#print kv
	key = kv.split('=')[0]
	value = kv.split('=')[1]
	#print key, value
	a = ""
	b = ""
	if D.has_key(key):
	    a,b = D[key]
	if isBase:
	    a = value
	else:
	    b = value
	D[key] = a,b

store(base_split, 1)
store(comp_split, 0)

#print D
for key, value in D.iteritems():
    base, comp = value
    if base != comp:
	print '%s %s %s' % (key, base, comp)

print

