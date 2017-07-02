"""
Written by Kevin Yang

Solution to LeetCode's "Add Two Numbers"

Runtime: 126 ms
Runtime beats 76.67 % of python submissions.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        if l1 or l2:
            head = ListNode(0)
        walker = head
        temp_sum = 0
        carry_over = 0 #either 0 or 1, since 2nd digit never > 1. Up to 9 + 9 = 18.
        while l1 or l2 or carry_over == 1:
            if l1 is None and l2 is None:
                temp_sum = 0
            elif l1 is None:
                temp_sum = l2.val
            elif l2 is None:
                temp_sum = l1.val
            else:
                temp_sum = l1.val + l2.val
            
            if carry_over == 1:
                temp_sum += 1
                carry_over = 0
                if l1 is None and l2 is None:
                    walker.val = 1
                    return head
            
            if temp_sum > 9:
                carry_over = 1
                walker.val = temp_sum - 10
            else:
                walker.val = temp_sum
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
            if l1 or l2 or carry_over == 1:
                walker.next = ListNode(0)
                walker = walker.next
            
        return head