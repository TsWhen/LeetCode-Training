# 迭代
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if not head:
            return head
        elif not head.next:
            return head
        node = head.next
        before_node = head
        head.next = None
        
        while node.next:
            
            next_node = node.next
            node.next = before_node
            before_node = node
            node = next_node
            
        node.next = before_node
        return node
            
            
# 递归写法，在head节点前设一个None节点
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:        
        curr_node = None
        
        return self.reverse(curr_node, head)
        
        # while next_node:
        #     temp = next_node.next
        #     next_node.next = curr_node
        #     curr_node = next_node
        #     next_node = temp
        # return curr_node
            
    def reverse(self, curr_node, next_node):
        if not next_node:
            return curr_node
        temp_node = next_node.next
        next_node.next = curr_node
        return self.reverse(next_node, temp_node)