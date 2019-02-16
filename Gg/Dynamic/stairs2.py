import sys

inp = sys.stdin.readlines()

stairs = {1: 1, 2: 2}

def stairsNum(n):
  #if n == 1 or n == 2: return n
  if n not in stairs:
    stairs[n] = stairsNum(n-1) + stairsNum(n-2)
  #return stairsNum(n-1) + stairsNum(n-2)
  return stairs[n]

for l in inp:
  if l[:-1].isdigit():
    num = int(l)
    print num, "   ", stairsNum(num) 
