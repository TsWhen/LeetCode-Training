
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        for i in range(32):
            
            bit_x = x % 2
            bit_y = y % 2
            if bit_x != bit_y:
                count+=1
            x >>= 1

            y >>= 1
        
        return count

# 求异或后统计有多少个1
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')