def avg(n):
    sum = 0
    c = 0
    
    for i in range(-100, 100):
        if i in n :
            c = c + 1
            sum = sum + i
    
    average = sum/c
    return average

nums = list(map(int, input().split()))

if len(nums) == 1:
    print(str(nums[0])+".00")

else:
    res = avg(nums)
    print(res)
