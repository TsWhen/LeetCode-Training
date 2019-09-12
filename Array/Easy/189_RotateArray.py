# 取模后判断需要旋转多少位，然后同时对两段list进行赋值
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        point = len(nums) - k
        nums[:k],nums[k:] = nums[point:] , nums[:point]
