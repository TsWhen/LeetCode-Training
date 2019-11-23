# 固定三元组中的一个值，将问题转化为两数相加得到特定值的问题
# 由于题目中不重复打印相同三元组，所以要添加判断，通过固定位置值来筛选

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solve_list = []
        num_dict = {}
        nums = sorted(nums)
        for i in range(len(nums)-2):
            
            if nums[i] in num_dict:
                continue
            else:
                num_dict[nums[i]] = 1
            second_num_dict = {}
            
            j = i+1
            k = len(nums) - 1
            second_num_dict = {}
            while j < k:
                if nums[j] in second_num_dict:
                    j+=1
                    continue
                value = nums[j] + nums[k] + nums[i]
                if value == 0:
                    solve_list.append([nums[i],nums[j],nums[k]])
                    second_num_dict[nums[j]] = 1
                    j += 1
                    k -= 1
                elif value > 0:
                    k -= 1
                else:
                    j += 1
                
        
        return solve_list
            