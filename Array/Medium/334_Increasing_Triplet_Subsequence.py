# 是否达到3的长度只与i位置上的数是否大于递增序列第二个数有关，一旦位置i的数小于当前序列中的某些数，将该个数更新到它最小的位置
# 最快解题的思路与本思路一致
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import sys
        num = 1
        first_pos = sys.maxsize
        second_pos = sys.maxsize
        
        for i in range(len(nums)):
            
            if nums[i] > second_pos:
                return True
            elif nums[i] == second_pos:
                continue
            else:
                if nums[i] > first_pos:
                    second_pos = nums[i]
                else:
                    first_pos = nums[i]
        
        return False