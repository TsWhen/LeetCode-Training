# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if not head:
            return head
        
        odd_node = head
        even_node = even_head = head.next
        next_node = even_node
        while next_node and next_node.next:
            
            odd_node.next = next_node.next
            odd_node = odd_node.next
            even_node.next = next_node.next.next
            even_node = even_node.next
            next_node = even_node
        
        odd_node.next = even_head
        
        return head
            
            