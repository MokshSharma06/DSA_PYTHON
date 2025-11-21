class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        max_len = 0  # Initialize max length to 0, not negative infinity
        hashmap = {}
        low = 0
        high = 0

        while high < n:
            if s[high] in hashmap and hashmap[s[high]] >= low:
                low = hashmap[s[high]] + 1
            hashmap[s[high]] = high  # Update last seen index
            max_len = max(max_len, high - low + 1)
            high += 1  # Don't forget to move high pointer to expand window

        return max_len

