import sys
import math

mat = sys.stdin.readlines()

mat = [ x[:-1] for x in mat ]

sizex = len(mat[0])
sizey = len(mat)

l = []
dx = {}
dy = {}
c = {}
#num = 0

def matrixf():
  num = 0
  for row in range(sizey):
    for col in range(sizex):
      if mat[row][col] == 'O':
        num+=1
	l.append(ptol(row, col))
	dx[ptol(row, col)] = []
        dy[ptol(row, col)] = []
        #c[ptol(row, col)] = 0
	#counter == 0
        cx = 0
	cy = 0
	for x in range(sizex):
          if x != col and  mat[row][x] == 'O':
            dx[ptol(row, col)].append(ptol(row, x))
	    #counter+=1
	    cx = 1
	for y in range(sizey):
          if y != row and  mat[y][col] == 'O':
            dy[ptol(row, col)].append(ptol(y, col))
  	    #counter+=1
	    cy = 1
	c[ptol(row, col)] = cx+cy
  state = 1
  while(state != 0):
    state = 0
    for orb in l:
      if c[orb] == 1:
	state = 1
	num = removeOrb(orb, num)
      elif state == 0:
	state = max(state, c[orb])
    if state == 2:
      num = removeOrb(l[0], num)
  #n = num
  return num

def removeOrb(o, num):
  if dx[o]:
    for XConnect in dx[o]:
      dx[XConnect].remove(o)
      if not dx[XConnect]:
        c[XConnect]-=1
  if dy[o]:
    for YConnect in dy[o]:
      dy[YConnect].remove(o)
      if not dy[YConnect]:
        c[YConnect]-=1

  del c[o]
  l.remove(o)
  #print num
  num-=1
  return num

def ptol(row, col):
  return row*sizex+col

def ltop(index):
  return index / sizex, index % sizex



for line in mat: print line
print ""

num = matrixf()
print num

