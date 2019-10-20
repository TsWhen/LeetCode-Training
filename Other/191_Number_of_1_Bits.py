class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = bin(n)
        count = 0
        for i in range(len(s)):
        
            if s[i] == '1':
                count += 1
        
        return count

#快速写法，结合位运算
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            if n %2 >0:
                count+=1
            n >>= 1
        return count