class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap={}
        for i, nums in enumerate (nums):
            complement = target - nums
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[nums]= i
        