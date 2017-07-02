"""
Written by Kevin Yang

Solution to LeetCode's "Valid Parentheses"

Runtime: 42 ms
Runtime beats 76.49 % of python submissions.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_symbs = {"{":"}", "[":"]", "(":")"}
        right_dict = {"}":0, "]":0, ")":0}
        ids = {"{":1, "[":2, "(":3, "}":1, "]":2, ")":3}
        
        stk = list()
        if s[0] not in left_symbs:
            return False
        for c in s:
            if c in left_symbs:
                stk.append(ids[c])
            elif len(stk) > 0 and ids[c] == stk[len(stk)-1]:
                stk.pop()
            else:
                return False
        if len(stk) > 0:
            return False
        return True