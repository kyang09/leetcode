"""
Written by Kevin Yang

Solution to LeetCode's "Count and Say"

Runtime: 42 ms
Runtime beats 82.33 % of python submissions.
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        seq = "1"
        for i in range(0, n-1):
            temp_c = seq[0]
            count = 1
            temp_ans = ""
            for j in range(1, len(seq)):
                if temp_c == seq[j]:
                    count += 1
                else:
                    temp_ans += (str(count) + temp_c)
                    temp_c = seq[j]
                    count = 1
            if temp_ans == "":
                seq = (str(count) + temp_c)
            else:
                seq = temp_ans + str(count) + temp_c
        
        return seq