"""
Written by Kevin Yang

Solution to LeetCode's "Reverse Integer"

Runtime: 52 ms
Runtime beats 74.09 % of python submissions.
"""

import math
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        retVal = 0
        temp = abs(x)
        while temp != 0:
            retVal = retVal * 10
            retVal = (retVal + (temp % 10))
            temp = temp / 10
        if retVal >= math.pow(2,31):
            return 0
        if x < 0:
            retVal = retVal * -1
        return retVal