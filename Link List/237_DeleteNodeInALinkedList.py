# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next:
            
            next_node = node.next
            if not node.next.next:
                node.next = None
            
            node.val = next_node.val
            # node.next = next_node.next
            node = next_node
            
# 较快写法,自己替代下一节点的值，实际情况是将下一个节点移出了链表
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next 