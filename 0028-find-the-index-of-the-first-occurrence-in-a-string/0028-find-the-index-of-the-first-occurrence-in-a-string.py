class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        M = len(haystack)
        N = len(needle)
        k = -1
        for i in range(M):
            if haystack[i:i+N] == needle:
                k = i
                break
                
        return k