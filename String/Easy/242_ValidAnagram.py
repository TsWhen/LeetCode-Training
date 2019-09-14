# 将两个字符串分别按照字符编码值进行排序，然后对比两个字符串是否相等
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        s.sort()
        s = ''.join(s)
        t = list(t)
        t.sort()
        t = ''.join(t)

        if s == t:
            return True

        return False

#使用Python中的计数器类Counter(继承于dict，用于统计元素出现次数)
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = Counter(s)
        y = Counter(t)
        return x ==y