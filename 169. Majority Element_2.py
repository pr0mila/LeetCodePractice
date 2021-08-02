class Solution(object):
    def majorityElement(self, nums):
        sum = {}
        for n in nums:
            if n not in sum:
                sum[n]=1
            else:
                sum[n] += 1
            if sum[n] > len(nums)/2:
                return n
"""
nums = [1,1,2,3,1]
obj=Solution()
print(obj.majorityElement(nums))

"""


