s = raw_input()


l = []

def permu(s, i):
  l = []
  if i==0:
    l.append(s)

  if i+1 >= len(s): return l

  if i+2 < len(s):
    l = l + permu(s, i+1)

  for index in range(i+1, len(s)):
    if s[i] != s[index]:
      tempS = s[:i] + s[index] + s[i+1:index] + s[i] + s[index+1:]
      #print "i: ", i, "index: ", index, "s: ", tempS
      l.append(tempS)
      l = l + permu(tempS, i+1)
  
  return l

k = set(permu(s, 0))
#print k
print ""
print "s size:", len(s)
print "num of permu", len(k)


