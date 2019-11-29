#正常层次遍历即可，对于每一层判断一次是否需要翻转

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res_list = []
        node_list = [root]
        pos = 0
        node_num = 1
        is_tra = False
        while pos < node_num:
            end_pos = node_num
            res = []
            for i in range(pos,end_pos):
                if node_list[i].left:
                    node_list.append(node_list[i].left)
                if node_list[i].right:
                    node_list.append(node_list[i].right)
                res.append(node_list[i].val)
            pos = end_pos
            if is_tra:
                res = res[::-1]
            res_list.append(res)
            is_tra = not is_tra
            node_num = len(node_list)
        return res_list