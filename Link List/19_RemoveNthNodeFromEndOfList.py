# 记录下当前已遍历序列的倒数第N个节点的父节点，然后到整个链表末端后将父节点的子节点设为倒数第N个节点的子节点
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        head_node = head
        replace_node = head
        before_node = None
        cur_node = head
        for i in range(n):
            cur_node = cur_node.next
        
        while cur_node:
            cur_node = cur_node.next
            before_node = replace_node
            replace_node = replace_node.next
        if not before_node:
            if not replace_node.next:
                return None
            replace_node.val = replace_node.next.val
            replace_node.next = replace_node.next.next
        else:
            before_node.next = replace_node.next
        # if not replace_node.next:
        #     replace_node.val = None
        #     replace_node.next = None
        # else:

        return head_node
# 较快写法
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head