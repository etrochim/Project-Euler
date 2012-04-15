#!/usr/bin/env python

import math

total = 0
for a in xrange(10, 1000000):
  mysum = sum([math.factorial( int(i) ) for i in list(str(a))])
  if a == mysum:
    total += a

print "Total is %d" % total
