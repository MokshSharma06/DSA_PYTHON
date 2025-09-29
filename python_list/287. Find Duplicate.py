class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dup=set()
        for number in nums:
            if number in dup:
                return number
            dup.add(number)
        return False