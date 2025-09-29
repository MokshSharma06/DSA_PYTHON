class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freq={}
        freq2={}

        for number in s:
            freq[number]=freq.get(number,0)+1
        for number in t:
            freq2[number]=freq2.get(number,0)+1
        
        if freq == freq2:
            return True
        return False

s = "anagram"
t = "nagaram"

Sol = Solution()
result = Sol.isAnagram(s,t)
print(result)
