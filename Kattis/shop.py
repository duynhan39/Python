import sys

l = [int(x) for x in sys.stdin.readlines()[1].split()]

l = sorted(l, reverse=True)

s=0
for i in range (2, len(l), 3):
  s+=l[i]

print s
 
