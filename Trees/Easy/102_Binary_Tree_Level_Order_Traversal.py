# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        value_list = []
        self.traversal([root],value_list)
        
        return value_list
        
    def traversal(self,node_list,value_list):
        
        if not node_list:
            return 
        
        next_node_list = []
        node_value_list = []
        
        for i in range(len(node_list)):
            
            node_value_list.append(node_list[i].val)
            
            if node_list[i].left:
                next_node_list.append(node_list[i].left)
            if node_list[i].right:
                next_node_list.append(node_list[i].right)
        
        value_list.append(node_value_list)
        
        self.traversal(next_node_list,value_list)
            
        