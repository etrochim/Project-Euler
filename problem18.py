#!/usr/bin/env python

def recurse(line, pos):
  if line + 1 < len(triangle):
    return max(triangle[line][pos] + recurse(line+1, pos), triangle[line][pos] + recurse(line+1, pos+1))
  else:
    return triangle[line][pos]

triangle = []
for line in open("problem18.txt", "r"):
  triangle.append([ int(x) for x in line.split()])

print recurse(0, 0)
