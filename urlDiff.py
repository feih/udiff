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

import json
data = []

def printer(param, base, comp):
    if base==None:
        base = ""
    if comp==None:
        comp = ""
    #print '%s %s %s' % (param, base, comp)
    data.append({"key" : param, "base" : base, "comp" : comp});

if base_schema != compare_schema:
    printer("scheme", base_schema, compare_schema);
if base_host != compare_host:
    printer("host", base_host, compare_host);
if base_port != compare_port:
    printer("port", base_port, compare_port);
if base_path != compare_path:
    printer("path", base_path, compare_path);
if base_frag != compare_frag:
    printer("fragment", base_frag, compare_frag);


for key, value in D.iteritems():
    base, comp = value
    if base != comp:
        base_ = "";
        comp_ = "";
        if len(base) != 0:
            base_ = ' '.join(base)
        if len(comp) != 0:
            comp_ = ' '.join(comp)
	#print '%s %s %s' % (key, base_, comp_)
        data.append( {'key' : key, "base" : base_, "comp" : comp_ })
#print # to test ajax timeout, comment this out
print json.dumps(data)

#TOOD
# 1. http://en.wikibooks.org/wiki/Statistical_Analysis:_an_Introduction_using_R?a=d&a=c
