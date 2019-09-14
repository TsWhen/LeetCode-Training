# 去除非数字和字符后统一改成小写，由首尾往中间进行比对，验证回文格式
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_str = ""
        for s_char in s:

            if 'a' <= s_char <= 'z' or '0' <= s_char <= '9':
                new_str += s_char

        str_len = len(new_str)
        for i in range(str_len // 2):

            if new_str[i] != new_str[str_len - 1 - i]:
                return False
        return True

# 将字符串逆向输出，与正向对比是否相同
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=re.sub(r'\W+',"",s)
        lnew=new.lower()
        rnew=lnew[::-1]
        if lnew==rnew:
            return True
        else:
            return False