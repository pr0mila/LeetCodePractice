class Solution(object):
    def remove_duplicates(self,nums):
        n = len(nums)

        if n == 0:
            return 0

        current_index = 1
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[current_index] = nums[i]
                current_index += 1

        return current_index

"""
nums = [1,1,2,3]
obj=Solution()
l = obj.remove_duplicates(nums)
print(nums[:l])
"""


