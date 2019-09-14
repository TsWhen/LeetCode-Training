# 遍历haystack逐个子串对比
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        needle_len = len(needle)
        for i in range(len(haystack) - needle_len + 1):

            if haystack[i:i+needle_len] == needle:
                return i
        if needle == haystack:
            return 0
        return -1 