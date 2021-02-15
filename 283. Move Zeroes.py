class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)
        non_zero = 0
        for n in nums:
            if n  != 0:
                nums[non_zero]=n
                non_zero+=1

        for zero in range (1,zero_count+1):
            nums[-zero]=0

"""
nums = [0,1,5,0,3,8,0,0,9]
ob1 = Solution()
ob1.moveZeroes(nums)
print(nums)
"""