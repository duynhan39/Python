#!/usr/bin/python

s1 = raw_input()
s2 = raw_input()

def checkSub():
  if len(s2) < len(s1): return False

  l = {}
  for each in s1:
    if each in l:
      l[each]+=1
    else:
      l[each]=1

  c = len(l)

  for i in range(0, len(s1)):
    if s2[i] in l:
      l[s2[i]]-=1
      if l[s2[i]] == 0:
        c -= 1
      elif l[s2[i]] == -1:
        c += 1
  if c==0: return True
  
  #print "c: ", c, ", l", l

  for j in range(len(s1), len(s2)):
    if s2[j-len(s1)] in l:
      l[s2[j-len(s1)]]+=1
      if l[s2[j-len(s1)]] == 0:
        c -= 1
      elif l[s2[j-len(s1)]] == +1:
        c += 1

    if s2[j] in l:
      l[s2[j]]-=1
      if l[s2[j]] == 0:
        c -= 1
      elif l[s2[j]] == -1:
        c += 1

    
    #print "c: ", c, ", l", l
 
    if c==0: return True



  return False


print checkSub()
