# BFS，利用list加下标移动实现队列效果

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        depth = 0
        node_queue = [root]
        point = 0
        
        while point < len(node_queue):
            
            queue_len = len(node_queue)
            for i in range(point,queue_len):
                
                if node_queue[i].left:
                    node_queue.append(node_queue[i].left)
                if node_queue[i].right:
                    node_queue.append(node_queue[i].right)
            point = queue_len
            depth += 1
        return depth