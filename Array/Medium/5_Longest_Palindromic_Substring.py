# 将输入字符串翻转，求取最长公共连续子序列，判断子序列起始下标是否相同
# 有很多更快速的写法和算法，后续进一步学习
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        pali_s = s[::-1]
        
        dp = [[0]*(len(s)+1) for i in range(len(s)+1)]
        
        max_len = 0
        start_pos = 0
        end_pos = 0
        for i in range(1,len(s)+1):
            
            for j in range(1,len(s)+1):
                s_pos = i-1
                pali_pos = j-1
                # 最长连续公共子序列
                if s[s_pos] == pali_s[pali_pos]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    
                    
                    if dp[i][j] > max_len:
                        #如果子序列起始下标相同他们才是回文
                        if (s_pos + 1 - dp[i][j]) == ((len(s)-1)-pali_pos):
                            start_pos = s_pos + 1 - dp[i][j]
                            end_pos = s_pos + 1
                            max_len = dp[i][j]
                else:
                    dp[i][j] = 0
        
        if max_len <1:
            return s[0]
        return s[start_pos:end_pos]
                    
                    
                    
                    