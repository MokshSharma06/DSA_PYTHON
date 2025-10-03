class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        frq={}

        for words in s:
            frq[words]=frq.get(words,0)+1
        for i, words in enumerate(s):
            if frq[words]==1:
                return i
        return -1
