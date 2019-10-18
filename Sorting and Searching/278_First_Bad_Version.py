# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# 二分查找
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        h = n
        while l!=h:
            if isBadVersion((l+h)//2):
                h = (l+h) // 2
            else:
                l = (l+h) // 2 + 1
        
        return l