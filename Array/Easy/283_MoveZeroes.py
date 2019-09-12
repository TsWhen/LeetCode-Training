# DP思想，将前一个序列长度的状态当成已经满足所有零在序列尾部，则再加入一个数字如果是非零只需和处于序列第一个0进行互换即可
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_zero_point = 0

        for i in range(len(nums)):

            if nums[i] != 0:
                nums[first_zero_point],nums[i] = nums[i],nums[first_zero_point]
                first_zero_point += 1
# 快速方法：思路一样，但是实现时不用每次都进行交换，只要对非零部分赋好值，最后再将其余部分赋0
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for n in nums:
            if n != 0:
                nums[i] = n
                i += 1
        
        for i in range(i, len(nums)):
            nums[i] = 0