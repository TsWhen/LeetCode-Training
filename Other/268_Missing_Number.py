class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for i in range(1,len(nums)+1):
            sum += i
        
        for i in range(len(nums)):
            sum -= nums[i]
        
        return sum