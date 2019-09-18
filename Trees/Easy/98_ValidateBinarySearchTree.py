# 中序遍历，获取从小到大的序列
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def LDR(node):
            if not node:
                return []

            return LDR(node.left)+[node.val]+LDR(node.right)
        LDR_list = LDR(root)
     
        for i in range(len(LDR_list) - 1):
            if LDR_list[i] >= LDR_list[i+1]:
                return False
        return True
    
    

# 递归，逐对比较
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        
        return self.helper(root, float('-inf'), float('inf'))
    
    def helper(self, node, low, high):
        
        if not node:
            return True
        
        if node.val >= high or node.val <= low:
            return False
        
        else:
            
            return self.helper(node.left, low, node.val) and self.helper(node.right, node.val, high)