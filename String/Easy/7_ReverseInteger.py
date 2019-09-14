# 通过bit_length获取输入整数二进制长度判断是否在正常范围内
class Solution:
    def reverse(self, x: int) -> int:
        
        if x < 0:
            x = -1 * int(str(x)[1:][::-1])
        else:
            x = int(str(x)[::-1])
        
        if x.bit_length() > 31:
            return 0
        return x