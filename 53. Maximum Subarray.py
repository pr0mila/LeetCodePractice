class Solution:
    def maxSubArray(self, nums):
        
""""
    def bruteforcemaxSubArray(self, nums):

        max_sum = float('-Inf')
        current_sum = float('-Inf')

        for i in range (len(nums)):
            current_sum = nums[i]
            if current_sum > max_sum:
                max_sum = current_sum
            for j in range (i+1, (len(nums))):
                current_sum += nums[j]
                if current_sum > max_sum:
                    max_sum=current_sum
        return max_sum
"""