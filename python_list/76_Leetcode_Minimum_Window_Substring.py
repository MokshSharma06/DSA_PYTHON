class Solution(object):
    def minWindow(self, s, t):
        m = len(s)
        low = 0
        high = 0
        hashmap = {}
        hashmap2 = {}
        min_len = float('inf')
        min_start = 0

        # Count frequency of characters in t
        for ch in t:
            hashmap2[ch] = hashmap2.get(ch, 0) + 1

        def is_valid(hashmap, hashmap2):
            for k in hashmap2:
                if hashmap.get(k, 0) < hashmap2[k]:
                    return False
            return True

        while high < m:
            hashmap[s[high]] = hashmap.get(s[high], 0) + 1

            while is_valid(hashmap, hashmap2):
                window_len = high - low + 1
                if window_len < min_len:
                    min_len = window_len
                    min_start = low
                hashmap[s[low]] -= 1
                if hashmap[s[low]] == 0:
                    del hashmap[s[low]]
                low += 1
            high += 1

        # Final result extraction
        return "" if min_len == float('inf') else s[min_start:min_start+min_len]
