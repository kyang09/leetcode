"""
Written by Kevin Yang

Solution to LeetCode's "Longest Substring Without Repeating Characters"

Runtime: 102 ms
Runtime beats 66.41 % of python submissions.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = dict() # Dictionary to keep track of the index of the repeated char
        cur_max = -1 # maximum length of substring 
        i = 0 # Counter for while loop
        head = 0 # Head of the substring
        counter = 0

        # Loop through the string O(N).
        while i < len(s):
            if s[i] in dic:
                dic_index = dic[s[i]]
                if dic_index < i and dic_index >= head:
                    if counter > cur_max:
                        cur_max = counter
                    counter -= ((dic_index - head) + 1)
                    head = dic_index + 1
            
            dic[s[i]] = i
            counter += 1
            i += 1
        
        if counter > cur_max:
            return counter
        return cur_max