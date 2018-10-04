R, C = int(input())

l = list()
count = [0,0,0,0,0]

for i in range(R):
	s = input()
	l.append(s)

for y in range(R-1):
	for x in range(C-1):
		if l[y][x]!='#' and l[y][x+1]!='#' and l[y+1][x]!='#' and l[y+1][x+1]!='#':
		:x	
