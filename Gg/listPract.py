l = [1, 3, 6, "LOL", "HI", "Bye"]

n = [ n+n for n in l if isinstance(n, int) ]

print n
