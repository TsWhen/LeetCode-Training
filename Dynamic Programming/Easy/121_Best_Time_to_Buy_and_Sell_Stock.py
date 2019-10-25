class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = 99999999
        max_value = 0
        
        
        for i in range(0,len(prices)):
            
            if min_price > prices[i]:
                
                min_price = prices[i]
            
            elif ((prices[i] - min_price) > max_value):
                
                max_value = prices[i] - min_price
                
        return max_value
            
            