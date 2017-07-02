"""
Written by Kevin Yang

Solution to LeetCode's "Palindrome Number"

Runtime: 212 ms
Runtime beats 82.94 % of python submissions.
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        intstr = str(x)
        strlen = len(intstr)
        #if lenstr % 2 == 0:
        #    for i in range(0, lenstr/2):
        #        if intstr[i] is not intstr[(lenstr - i) - 1]:
        #            return False
        #else:
        #    for i in range(0, (lenstr-1)/2):
        #        if intstr[i] is not intstr[(lenstr - i) - 1]:
        #            return False
        
        for i in range(0, (strlen - (strlen % 2))/2):
            if intstr[i] is not intstr[strlen - i - 1]:
                return False
        return True