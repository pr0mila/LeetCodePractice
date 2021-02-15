class Solution(object):
    def majorityElement(self, nums):

        return sorted(nums)[len(nums) // 2]

nums = [1,1,2,2,2,2,3,1]
obj=Solution()
print(obj.majorityElement(nums))
