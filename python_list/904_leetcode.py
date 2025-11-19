class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        n =len(fruits)
        low =0
        high =0
        freq={}
        count = -1
        k=2
        
        while(high < n):
            freq[fruits[high]]=freq.get(fruits[high],0)+1
            while len(freq)>k:
                freq[fruits[low]]-=1
                if freq[fruits[low]]==0:
                    del freq[fruits[low]]
                low+=1
            if len(freq)<=k:
                count =max(count,high-low+1)
            high+=1
        return count
