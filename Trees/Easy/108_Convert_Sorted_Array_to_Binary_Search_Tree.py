# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = self.select_node(nums)
        return root
    
    def select_node(self,nums):
        
        if not nums:
            return 
        
        pos = len(nums) // 2
        value = nums[len(nums) // 2]
        
        node = TreeNode(value)
        
        node.left = self.select_node(nums[:pos])
        node.right = self.select_node(nums[pos+1:])
        
        return node
        