def singleNumber(nums):
    s=0
    for i in nums:
        s^=i
    return s

nums=[1,2,4,2,1]
print(singleNumber(nums))