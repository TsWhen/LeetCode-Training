# 使用Fisher–Yates shuffle 洗牌算法洗牌算法进行shuffle操作

import random
class Solution:

    def __init__(self, nums: List[int]):
        
        self.nums = nums
        self.nums_len = len(nums)
        self.pos_list = [i for i in range(self.nums_len)]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        i = 0
        while i < self.nums_len:
            
            if self.pos_list[i] != i:
                pos = self.pos_list[i]
                self.nums[i],self.nums[pos] = self.nums[pos],self.nums[i]
                
                #self.pos_list[i],self.pos_list[self.pos_list[i]] = self.pos_list[self.pos_list[i]],self.pos_list[i]
                self.pos_list[i],self.pos_list[pos] = self.pos_list[pos],self.pos_list[i]
                
            else:
                i += 1
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        
        for i in range(self.nums_len - 1, -1 ,-1):
            
            pos = random.randint(0,i)
            self.nums[i],self.nums[pos] = self.nums[pos],self.nums[i]
            self.pos_list[i],self.pos_list[pos] = self.pos_list[pos],self.pos_list[i]
        
        
        return self.nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

# 快速解法
from itertools import permutations

class Solution:

    def __init__(self, nums: List[int]):
        self._orig = nums
        self._current = nums
        self._perm = permutations(nums)
        next(self._perm)
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self._current = self._orig
        return self._current

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        try:
            self._current = next(self._perm)
        except:
            self._perm = permutations(self._orig)
            return self.shuffle()
        return self._current