s1 = raw_input()
s2 = raw_input()


table = [[0 for col in range(len(s1)+1)] for row in range(len(s2)+1)]

longest = 0

for row in range(1, len(s2)+1):
  for col in range(1, len(s1)+1):
    if s1[col-1] == s2[row-1]:
      table[row][col] = table[row-1][col-1] + 1
      longest = max(longest, table[row][col])

print longest
