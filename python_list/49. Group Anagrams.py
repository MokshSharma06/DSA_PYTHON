class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap={}

        for words in strs:
            key = "".join(sorted(words))

            if key not in hashmap:
                hashmap[key]=[]
            hashmap[key].append(words)

        return list(hashmap.values())


        