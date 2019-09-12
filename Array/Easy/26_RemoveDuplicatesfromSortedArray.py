# 我的代码
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        new_len = 1
        
        if not nums:
            return 0
        
        cur_num = nums[0]
        for next_num in nums[1:]:
            if (cur_num ^ next_num == 0):
                del nums[new_len]
                continue
            new_len += 1
            cur_num = next_num
        
        return len(nums)

#  快于 99.91%代码
class Solution(object):
    def removeDuplicates(self, nums):
      tracker=0
      for r in range (1,len(nums)):
        if nums[r]!=nums[tracker]:
          tracker+=1
          nums[tracker]=nums[r]
      return tracker+1