#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        
        if not l1:
            return l2
        elif not l2:
            return l1
        
        if l1.val < l2.val:
            head = l1
        else:
            head = l2
        while (not l1) or (not l2):
            
            if l1.val < l2.val:
                
                l1_next = l1.next
                l1.next = l2
                l1 = l1_next
            else:
                l2_next = l2.next
                l2.next = l1
                l2 = l2_next
        return head  

