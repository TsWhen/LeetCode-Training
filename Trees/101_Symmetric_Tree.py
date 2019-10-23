

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        node_queue = [root,root]
        pos = 0
        
        while pos != len(node_queue):
            
            node_one = node_queue[pos]
            node_two = node_queue[pos+1]
            
            pos += 2
            if (not node_one) and (not node_two):
                continue
            elif node_one and node_two:
                
                if node_one.val != node_two.val:
                    return False
            else:
                return False
            
            node_queue.append(node_one.left)
            node_queue.append(node_two.right)
            node_queue.append(node_one.right)
            node_queue.append(node_two.left)
            
        return True
                    
                
        

#快速写法 递归
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.helper(root.left, root.right)
        return True
    
    def helper(self, p, q):
        if p == None and q == None: return True
        if p and q and p.val == q.val:
            return self.helper(p.left, q.right) and self.helper(p.right, q.left)
        return False