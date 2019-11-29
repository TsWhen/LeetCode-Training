# 迭代的思路就是通过栈，现将子树父节点按中序遍历顺序放入栈中，然后is_naive标识是否是从栈中弹出的，是的话不再遍历其左子树

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [None]
        node = root
        res_list = []
        is_naive = True
        while stack or node:

            if is_naive and node.left:
                stack.insert(0,node)
                node = node.left
                is_naive = True
            elif node.right:
                res_list.append(node.val)
                # stack.insert(0,node.right)
                node = node.right
                is_naive = True
            else:
                res_list.append(node.val)
                node = stack.pop(0)
                is_naive = False
        
        return res_list
            