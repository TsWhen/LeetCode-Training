class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        elif len(nums) > 1 and nums[1] < nums[0]:
            
            nums[1] = nums[0]
        
        for i in range(2,len(nums)):
            
            if nums[i-1] > nums[i] + nums[i-2]:
                
                nums[i] = nums[i-1]
            else:
                nums[i] += nums[i-2]
        
        return nums[len(nums)-1]
            