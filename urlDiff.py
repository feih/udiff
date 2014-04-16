#!/usr/bin/python

import sys
from urlparse import urlparse

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

b = urlparse(baseline);
c = urlparse(compare);

#hostname
base_host = b.hostname
compare_host = c.hostname
#port
base_port = b.port;
compare_port = c.port;
#path
base_path = b.path;
compare_path = c.path;
#fragment
base_frag = b.fragment;
compare_frag = c.fragment;

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

if base_host != compare_host:
    print 'host %s %s' % (base_host, compare_host);
if base_port != compare_port:
    print 'port %s %s' % (base_port, compare_port);
if base_path != compare_path:
    print 'path %s %s' % (base_path, compare_path);
if base_frag != compare_frag:
    print 'fragment %s %s' % (base_frag, compare_frag);

for key, value in D.iteritems():
    base, comp = value
    if base != comp:
	print '%s %s %s' % (key, base, comp)
