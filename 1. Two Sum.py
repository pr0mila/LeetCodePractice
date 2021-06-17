class Solution:

    def twoSum(self, nums, target):
        complementMap = dict()
        for i in range(len(nums)):
            num = nums[i]
            #print((num))
            complement = target - num
            #print((complement))
            #print((complementMap))
            if num in complementMap:
                #print(complementMap[num],i)
                return [complementMap[num],i]
            else:
                complementMap[complement]=i
               # print(complementMap[complement])
            #print((complementMap))
"""
    def bruteforcetwoSum(self, nums, target) :
        for i in range (len(nums)):
            for j in range(i+1,len(nums)):
                sum = nums[i]+nums[j]
                if(sum == target):
                    return i,j
nums = [3,2,4]
target = 6
obj=Solution()
obj.twoSum(nums,target)
"""