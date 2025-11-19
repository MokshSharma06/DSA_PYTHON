class Solution(object):
    def characterReplacement(self, s, k):
        max_count = 0
        max_len=0
        low = 0
        freq = {}
        high =0
        n =len(s)
        
        while high <n:
            freq[s[high]] = freq.get(s[high], 0) + 1
            max_count = max(max_count, freq[s[high]])
            
            if high - low + 1 - max_count > k:
                freq[s[low]] -= 1
                low += 1
            max_len = max(max_len, high - low + 1)
            high+=1

                
        return max_len
