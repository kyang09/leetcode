"""
Written by Kevin Yang

Solution to LeetCode's "Remove Duplicates from Sorted Array"

Runtime: 133 ms
Runtime beats 19.06 % of python submissions.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        exist_set = set()
        i = 0
        while i < len(nums):
            if nums[i] in exist_set:
                nums.pop(i)
                i -= 1
            else:
                exist_set.add(nums[i])
            i += 1