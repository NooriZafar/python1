class Solution:
    #def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(nums,target):
        for i in range(len(nums)):
            first=nums[i]
            for j in range(1,len(nums)):
                second=nums[j]
                if first+second==target:
                    return [i,j]
        return[-1,-1]

nums=[1,2,3,7,8]
target=5

twoSum(nums,target)
