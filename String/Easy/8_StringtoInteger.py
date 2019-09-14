# 对无需转换的条件进行判断，然后遍历去除有效数字字串，转换
class Solution:
    def myAtoi(self, str: str) -> int:
        
        str = str.strip()

        int_str = ""
        is_positive = True
        if str == "":
            return 0
        elif str[0] == '-':
            is_positive = False
        elif '0' <= str[0] <= '9':
            str = '+' + str
        elif str[0] != '+':
            return 0

        for s_char in str[1:]:

            if '0' <= s_char <= '9':
                int_str += s_char
            else:
                break
        if int_str == "":
            return 0
        num = int(int_str)
        if not is_positive:
            num = -1 * num
            return max(-0x80000000,num)

        return min(0x7fffffff,num)

# 更好的编程技巧
class Solution:
    def myAtoi(self, str: str) -> int:
        import re
        out = str.strip()
        out = re.findall("^[+-]\d+|^\d+", out)
        try:
            out = int(out[0])
        except:
            out = 0
        return min(max(-2**31, out), 2**31-1)