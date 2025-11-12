class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n =len(nums)
        low = 0
        high =1
        count =1

        while high <n:
            if nums[low]==nums[high]:
                high+=1
            elif nums[low]!=nums[high]:
                low+=1
                nums[low]=nums[high]
                high+=1
                count+=1
        return count
        