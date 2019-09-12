# 使用字典/hash 做映射判断是否有重复值
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        num_dict = {}

        for num in nums:

            if num_dict.__contains__(num):
                return True

            num_dict[num] = 1

        return False

# 快速方法：利用set数据结构的特点，判断前后长度是否一致
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))