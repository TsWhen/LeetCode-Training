# 任选一个字符串逐位判断是否位于公共前缀中
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if strs == []:
            return ""
        min_len = 0xffff
        for string in strs:
            if min_len > len(string):
                min_len = len(string)

        list_len = len(strs)
        last_point = 0
        for i in range(min_len):
            sub_char = strs[0][i]
            for j in range(1,list_len):
                if sub_char != strs[j][i]:
                    return strs[j][:last_point]
            last_point = i + 1

        return strs[0][:last_point]