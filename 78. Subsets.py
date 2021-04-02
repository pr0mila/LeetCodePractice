class Solution:
    def subsets(self, nums):
        results = [[]]

        for num in nums:
            results += [i + [num] for i in results]

        return results
