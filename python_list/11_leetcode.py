class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        low =0
        high =n-1
        max_area =0
        while low <high:
            width = high - low
            current_area = width * min(height[low],height[high])
            max_area= max(max_area,current_area)
            if height[low]<height[high]:
                low+=1
            else:
                high-=1
        return max_area 
