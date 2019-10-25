class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        for i in range(1,len(nums)):
            
            if nums[i-1] < 0:
                continue
            else:
                nums[i] += nums[i-1]
        
        max_value = nums[0]
        for i in range(1,len(nums)):
            
            if max_value < nums[i]:
                max_value = nums[i]
        
        return max_value