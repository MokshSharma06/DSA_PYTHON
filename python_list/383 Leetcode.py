class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        frq2={}
        
        for j in magazine:
            frq2[j]=frq2.get(j,0)+1

        for i in ransomNote:
            if frq2.get(i,0)==0:
                return False
            frq2[i]-=1
        return True