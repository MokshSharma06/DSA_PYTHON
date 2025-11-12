class Solution(object):
    def pivotIndex(self, nums):
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n

        # Build prefix sum
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        # Build suffix sum
        suffix[n - 1] = nums[n - 1]
        for j in range(n - 2, -1, -1):
            suffix[j] = suffix[j + 1] + nums[j]

        # Find the index where prefix == suffix
        for k in range(n):
            if prefix[k] == suffix[k]:
                return k
        return -1
