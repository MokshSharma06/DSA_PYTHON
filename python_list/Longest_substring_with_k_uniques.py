class Solution:
    def longestKSubstr(self, s, k):
        # code here
        
        n =len(s)
        low =0
        high =0
        freq={}
        count = -1
        
        while(high < n):
            freq[s[high]]=freq.get(s[high],0)+1
            while len(freq)>k:
                freq[s[low]]-=1
                if freq[s[low]]==0:
                    del freq[s[low]]
                low+=1
            if len(freq)==k:
                count =max(count,high-low+1)
            high+=1
        return count
      
