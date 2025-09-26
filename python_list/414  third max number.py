class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        if len(nums) <3:
            return max(nums)

        biggest = max(nums)
        second_biggest = max(
            x for x in nums
            if x !=biggest
        )
        third_biggest = max(
            x for x in nums if
            x != biggest and x!= second_biggest
        )
        return third_biggest
    
obj = Solution()
result = obj.thirdMax([
    4,5,6
])

print(result)