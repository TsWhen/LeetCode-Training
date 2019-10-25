# 到每个位置上的时候计算保存从当前位置最远可以到什么位置
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return True
        
        for i in range(1,len(nums)):
            
            if nums[i - 1] < i:
                
                return False
            
            else:
                
                nums[i] = max((i + nums[i]),nums[i-1])
        
        return True
        