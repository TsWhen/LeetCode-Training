# 统计每个字符出现次数，然后再一次遍历字符串，返回第一个出现次数为1的
class Solution:
    def firstUniqChar(self, s: str) -> int:

        num_dict = {}
        for i in range(len(s)):
            if s[i] not in num_dict.keys():
                num_dict[s[i]] = 1
            else:
                num_dict[s[i]] += 1

        for i in range(len(s)):

            if num_dict[s[i]] == 1:
                return i

        return -1

# 通过set找出需要判断的字符，然后统计字符个数，如果为1 就返回索引
class Solution:
    def firstUniqChar(self, s: str) -> int:
        return min([s.index(char) for char in set(s) if s.count(char) == 1] or [-1])