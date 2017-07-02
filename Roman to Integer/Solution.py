"""
Written by Kevin Yang

Solution to LeetCode's "Roman To Integer"

Runtime: 128 ms
Runtime beats 93.87 % of python submissions.
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 0:
            return 0
        
        alphab = ["I", "V", "X", "L", "C", "D", "M"]
        valArr = [1,    5,  10,  50,  100, 500, 1000]
        numerDict = dict()
        numerDict[alphab[0]] = 1

        for i in range(1, len(alphab)):
            numerDict[alphab[i]] = valArr[i]
        
        prevNumer = s[0]
        ans = numerDict[prevNumer]
        
        for j in range(1, len(s)):
            if s[j] not in numerDict: # if key not in dictionary
                return 0
            preVal = numerDict[prevNumer]
            sVal = numerDict[s[j]]
            if preVal >= sVal:
                ans += sVal
            else:
                ans = (ans - preVal) + (sVal - preVal)
            prevNumer = s[j]
        return ans