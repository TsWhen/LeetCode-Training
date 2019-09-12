# 通过映射将已扫描过的数存于字典/hash表中，然后判断当前数所需的另一个值是否存在于表中
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):

            need_num = target - nums[i]
            if nums_dict.__contains__(need_num):
                return [nums_dict[need_num],i]
            nums_dict[nums[i]] = i