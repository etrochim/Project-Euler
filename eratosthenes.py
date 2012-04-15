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
    return set([i for i in candidates[2:] if i])

def rotate(x, y=1):
   if len(x) == 0:
      return x
   y = y % len(x) # Normalize y, using modulo - even works for negative y
   return x[y:] + x[:y]

primes = eratosthenes_sieve(1000000)

for i in primes:
  istr = str(i)
  a = list(istr)
  rotated = rotate(a)
  f = 1
  while istr != ''.join(rotated):
    if int(''.join(rotated)) not in primes:
      f = 0
      break
    else:
      rotated = rotate(rotated)
  if f:
    print i


