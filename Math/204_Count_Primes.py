# 从2遍历至根号n，将其所有倍数标记，没被标记的是素数
import math
class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n < 3:
            return 0
        elif n == 3:
            return 1
        elif n == 4:
            return 2
        
        res = [0] * (n)
        
        for i in range(2,int(math.sqrt(n)+1)):
            
            j = 2
            while i*j < n:
                
                res[i*j] = 1
                j += 1
        
        count = 0
        for i in range(2,n):
            
            if res[i] == 0:
                count += 1
        return count


#快速写法
class Solution:
    def countPrimes(self, n: int) -> int:
        #120ms example, try it
        if n < 2:
            return 0
        
        strikes = [1] * n

        strikes[0] = 0
        strikes[1] = 0
        
        for i in range(2, int(n**0.5)+1):
            if  strikes[i] != 0:
                strikes[i*i:n:i] = [0] * ((n-1-i*i)//i + 1)

        return sum(strikes)