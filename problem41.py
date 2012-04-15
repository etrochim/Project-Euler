#!/usr/bin/env python

def eratosthenes_sieve(n):
    # Create a candidate list within which non-primes will be
    # marked as None; only candidates below sqrt(n) need be checked. 
    candidates = list(range(n+1))
    fin = int(n**0.5)
 
    # Loop over the candidates, marking out each multiple.
    for i in xrange(2, fin+1):
        if candidates[i]:
            candidates[2*i::i] = [None] * (n//i - 1)
 
    # Filter out non-primes and return the list.
    return [i for i in candidates[2:] if i]

def is_pandigital(n):
  return set(str(n)) == set([str(i) for i in range(1, len(str(n))+1)])

for i in reversed(eratosthenes_sieve(100000000)):
  if is_pandigital(i):
    print "Found %d" % i
    break

