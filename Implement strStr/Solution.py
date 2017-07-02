"""
Written by Kevin Yang

Solution to LeetCode's "Implement strStr()"

Runtime: 48 ms
Runtime beats 60.66 % of python submissions.
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if (len(needle) == 0 and len(haystack) == 0) or (len(needle) == 0 and len(haystack) > 0):
            return 0
        elif len(needle) > len(haystack):
            return -1
        else:
            for i in range(0, len(haystack)):
                if len(haystack) - i < len(needle):
                    return -1
                if haystack[i] == needle[0]:
                    j = 0
                    while j < len(needle):
                        if haystack[i + j] != needle[j]:
                            break
                        j += 1
                    if j == len(needle):
                        return i
        return -1