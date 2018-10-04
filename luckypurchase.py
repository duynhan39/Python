n = int(input())
first = True
min=0
name=""
for _ in range(n):
    qualified=True
    lapname, lapprice = input().split()
    num4=0
    num7=0
    for i in lapprice:
        if i=='4':
            num4+=1
        elif i=='7':
            num7+=1
        else:
            qualified=False
            continue
        if qualified and num4==num7 and first:
            min=int(lapprice)
            first=False
        elif qualified and num4==num7:
            if int(lapprice)<min:
                name=lapname
            
if first:
    print(-1)
else:
    print(name)

