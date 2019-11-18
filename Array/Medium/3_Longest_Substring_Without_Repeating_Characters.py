# dp思想，以第i字符为结尾的子串长度
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        
        dp = [""]
        pos = 0
        for i in range(len(s)):
            c = s[i]
            tmp = dp[pos].rfind(c)
            if tmp == -1:
                dp.append(dp[pos]+c)
            else:
                dp.append(dp[pos][tmp+1:] + c)
            pos += 1
            if len(dp[pos]) > max_len:
                max_len = len(dp[pos])
        
        return max_len