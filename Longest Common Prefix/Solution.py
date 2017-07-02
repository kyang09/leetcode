"""
Written by Kevin Yang

Solution to LeetCode's "Longest Common Prefix"

Runtime: 42 ms
Runtime beats 80.68 % of python submissions.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        
        prefix = ""
        comp_prefix = ""
        
        stringList = list(strs)
        stringList.sort()
        
        for i in range(0, len(stringList[0])):
            j = 0
            comp_prefix =  stringList[0][i]
            for j in range(1, len(stringList)):
                if comp_prefix != stringList[j][i]:
                    return prefix

            prefix += comp_prefix

        return prefix