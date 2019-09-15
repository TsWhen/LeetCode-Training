# 快慢指针思想，如若有环必然相遇

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        fast = slow = head
        
        while fast and slow:
            try:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    return True
            except:
                return False
        return False

# 对于可能出现None异常的处理
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False