#!/usr/bin/env python

def d(n):
  return sum([i for i in xrange(1, n/2+1) if n % i == 0])

mysum = 0
for a in xrange(1, 10000):
  b = d(a)
  i = d(b)
  if i == a and a != b:
    print "Found pairs %d, %d" % (a, b)
    mysum += a + b

print "Sum is %d" % (mysum / 2)
