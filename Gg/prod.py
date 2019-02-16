#!/usr/bin/python

import sys

a = list(map(int, raw_input().split()))
print a

b = [None]*len(a)
b[0] = a[0]

for i in range(1, len(a)-1):
  b[i] = b[i-1] * a[i]

b[-1] = b[-2]
acc = a[-1]
for i in range(len(a)-2, 0, -1):
  b[i] = b[i-1] * acc
  acc *= a[i]

b[0] = acc

print b

