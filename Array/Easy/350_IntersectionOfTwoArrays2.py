# 将其中一个list映射到字典中，然后逐个排查另一个list中的每个元素
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = {}
        union = []

        for num in nums1:
            if nums1_dict.__contains__(num):
                nums1_dict[num] += 1
                continue
            nums1_dict[num] = 1

        for num in nums2:
            if nums1_dict.__contains__(num):
                if nums1_dict[num] > 0:
                    nums1_dict[num] -= 1
                    union.append(num)
        return union