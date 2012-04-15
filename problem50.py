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
    return sorted([i for i in candidates[2:] if i])

primes = eratosthenes_sieve(1000000)
primesset = set(primes)

for i in primes:

