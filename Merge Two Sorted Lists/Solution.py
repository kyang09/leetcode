"""
Written by Kevin Yang

Solution to LeetCode's "Merge Two Sorted Lists"

Runtime: 52 ms
Runtime beats 70.37 % of python submissions.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return []
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            first = l1
            second = l2
            ret_list = ListNode(0)
            ret_travel = ret_list
            while first != None and second != None:
                if first.val <= second.val:
                    ret_travel.next = ListNode(first.val)
                    first = first.next
                else:
                    ret_travel.next = ListNode(second.val)
                    second = second.next
                ret_travel = ret_travel.next
            
            if second != None:
                ret_travel.next = second
            elif first != None:
                ret_travel.next = first
            
            return ret_list.next