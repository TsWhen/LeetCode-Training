class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        reverse_num = n % 2
        
        for i in range(31):
            
            reverse_num <<= 1
            n >>= 1
            bit_num = n % 2
            reverse_num += bit_num
        
        return reverse_num