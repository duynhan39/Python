t=int(input())
for _ in range(t):
    n=int(input())
    line=input()
    nums = [int(i) for i in line.split() ]
    min=nums[0]
    max=min
    for __ in range(1,n-1):
        tem = nums[__]
        if tem<min:
            min=tem
        if tem>max:
            max=tem
    print(max-min)
    del nums
