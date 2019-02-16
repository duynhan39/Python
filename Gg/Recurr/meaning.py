import sys
def wordBreak(s, words):
    result = []
    fi = False
    if s in words:
	#print "s", s
        result.append(s)
	return result, True
    for i in range(1, len(s)):
	if s[:i] in words:
	  res, fi = wordBreak(s[i:], words)
	  if fi:
            result += [s[:i]] + res
    #result += [ [s[:i]] + [word for word in wordBreak(s[i:], words)] for i in range(1,len(s)) if s[:i] in words]
    
    return result, fi


words = ['this', 'i', 'is', 'hi', 'bye', 'a', 'word', 'the', 'a', 'ab', 'abc', 'd']


input_str = sys.stdin.readlines()

print input_str

for l in input_str:
  if l == "\n":
    continue
  l = l[:-1]
  print "Input:", l
  print "Output:", wordBreak(l, words)[0]
  print ""
