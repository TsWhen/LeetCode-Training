# 寻找中间节点，然后将后半段翻转，对比两个链表

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        if not head:
            return True
        elif not head.next:
            return True
        
        node = head
        counter = 0
        while node:
            
            counter += 1
            node = node.next
        
        sub_head = head
        for i in range((counter // 2)+(counter % 2)) :
            sub_head = sub_head.next
        
        bd_node = None
        while sub_head.next:
            
            fd_node = sub_head.next
            sub_head.next = bd_node
            bd_node = sub_head
            sub_head = fd_node
        sub_head.next = bd_node
        
        fd_node = head
        bd_node = sub_head

        while bd_node:
            
            if fd_node.val != bd_node.val:
                return False
            bd_node = bd_node.next
            fd_node = fd_node.next
        return True
            

#思路相同，寻找中间节点方法不太一样
class Solution:
    def isPalindrome(self, head):
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        # compare the first and second half nodes
        while node: # while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True