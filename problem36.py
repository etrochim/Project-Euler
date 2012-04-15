#!/usr/bin/env python

def is_palindrome(string):
  if string[::-1] == string:
    return True
  return False

sum = 0
for i in xrange(1, 1000000, 2):
  if is_palindrome(str(i)) and is_palindrome(bin(i).replace('0b', '')):
    sum += i

print "Sum is %d" % sum
