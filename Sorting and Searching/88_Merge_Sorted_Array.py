class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        for i in range(m,m+n):

            for j in range(i,0,-1):

                if nums1[j] < nums1[j-1]:
                    nums1[j],nums1[j-1] = nums1[j-1],nums1[j]