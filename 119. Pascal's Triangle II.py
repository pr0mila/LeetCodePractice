class Solution:
    def generate(self, rowIndex):
        row = [1]

        for x in range(1, rowIndex + 1):
            row.append(row[x-1] * (rowIndex - x + 1) // x)
        return row

"""
row =5
obj = Solution()
print(obj.generate(row))
"""