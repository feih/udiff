#!/usr/bin/python

import sys
import urlparse

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

b = urlparse.urlparse(baseline);
c = urlparse.urlparse(compare);

#schema
base_schema = b.scheme
compare_schema = c.scheme
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

base_params = b.query;
comp_params = c.query;

D = dict()

def store(params, isBase):
    params = urlparse.parse_qs(params)
    #print params

    for k  in params:
	#print kv
	key = k
	value = params[key]
	#print key, value
	a = ""
	b = ""
	if D.has_key(key):
	    a,b = D[key]
	if isBase:
	    a = value
	else:
	    b = value
        # store it back
	D[key] = a,b

store(base_params, 1)
store(comp_params, 0)

#print D

if base_schema != compare_schema:
    print 'scheme %s %s' % (base_schema, compare_schema);
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
	print '%s %s %s' % (key, base[0], comp[0])
print
