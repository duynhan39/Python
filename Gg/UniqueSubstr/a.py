import sys

l = raw_input()

d = {}

for i in range(len(l)):
  if l[i] not in d:
    d[l[i]] = [-1, i]
  else:
    d[l[i]].append(i)

for letter in d:
  d[letter].append(len(l))

total = 0
for letter in d:
  for index in range(1, len(d[letter])-1):
    total += (d[letter][index] - d[letter][index-1])*(d[letter][index+1] - d[letter][index])

print total
  
  

