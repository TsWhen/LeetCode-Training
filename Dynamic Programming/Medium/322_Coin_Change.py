class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount < 1:
            return 0
        
        dp = [(amount+1)] * amount
        
        for i in range(len(coins)):
            
            if coins[i] > amount:
                continue
            dp[coins[i] - 1] = 1
        
        for i in range(amount):
            
            for j in range(len(coins)):
                
                if i < coins[j]:
                    
                    continue
                
                dp[i] = min(dp[i],dp[i - coins[j]] + 1)
        
        if dp[amount-1] > amount:
            return -1
        return dp[amount-1]
        