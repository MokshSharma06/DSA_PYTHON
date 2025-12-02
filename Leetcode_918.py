class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum =nums[0]
        min_sum=nums[0]
        current_max =nums[0]
        current_min =nums[0]
        res =nums[0]
        total_sum =nums[0]

        for i in nums[1:]:
            total_sum += i

            current_max = max(i,current_max+i)
            max_sum =max(current_max, max_sum)

            current_min=min(i,current_min+i)
            min_sum =min(current_min,min_sum)

            option3 = total_sum-min_sum

            res =max(max_sum,option3)

        if total_sum== min_sum:
            return max_sum
        else:
            return res




