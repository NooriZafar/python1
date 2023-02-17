def rob(nums):
    prev1=0
    prev2=0
    for i in range(0,len(nums)):
        temp=prev1
        prev1=max(prev2+nums[i],prev1)
        prev2=temp
    return prev1
s=[1,2,6,3]
print(rob(s))
