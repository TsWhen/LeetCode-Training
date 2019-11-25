# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        add_one = 0
        root = l1
        while True:
            
            value = l1.val + l2.val + add_one
            l1.val = value % 10
            add_one = value // 10
            
            if l1.next and l2.next:
                l1 = l1.next
                l2 = l2.next
            else: 
                if l2.next:
                    l1.next = l2.next
                while add_one == 1:
                    if l1.next:
                        l1 = l1.next
                        add_one = (l1.val + 1) // 10
                        l1.val = (l1.val + 1) % 10
                        
                    else:
                        l1.next = ListNode(1)
                        add_one = 0
            
                break
        return root
            
            