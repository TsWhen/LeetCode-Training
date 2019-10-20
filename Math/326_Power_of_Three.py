# 注意计算机中数字的表式，对数，除法计算后未必能够表示成整数

import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        return n > 0 and 3 ** round(math.log(n, 3)) == n