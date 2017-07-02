"""
Written by Kevin Yang

Solution to LeetCode's "Two Sum"

Runtime: 42 ms
Runtime beats 83.48 % of python submissions.
"""

import math
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()
        val = 0
        for i in range(0, len(nums)):
            val = target - nums[i]
            if val in dic and i != dic[val]:
                return [dic[val], i]
            dic[nums[i]] = i