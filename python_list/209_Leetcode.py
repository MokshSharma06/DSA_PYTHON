class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        low =0
        high =0
        min_len = float('inf')
        summ=0

        while(high <n):
            summ+=nums[high]
            while(summ>=target):
                length = high-low+1
                min_len =min(min_len,length)
                summ-=nums[low]
                low+=1
            high+=1
        return min_len if min_len <= n else 0
        
