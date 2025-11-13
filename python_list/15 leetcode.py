class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n =len(nums)
        res=[]
        nums.sort()
        for i in range(n-2):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            left = i+1
            right =n-1
            target = -1 * nums[i]

            while (left<right):
                S=nums[left]+nums[right]
                if S==target:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while (left <n  and nums[left]==nums[left-1]):
                        left+=1
                    while (right>=0 and nums[right]==nums[right+1]):
                        right-=1
                elif(S>target):
                    right-=1
                else:left+=1
        return res