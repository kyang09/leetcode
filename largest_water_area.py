import math

class Solution(object):
    def find_max_lines(self, height):
        if len(height) == 1:
            return height[0]
        else:
            left = find_max_lines(height[:(math.floor(len(height)/2))-1])
            right = find_max_lines(height[(math.floor(len(height)/2)):])
            
            return
    
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        return find_max_lines(height)