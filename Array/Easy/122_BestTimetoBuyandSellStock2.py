# 寻找所有的上涨阶段极大值与极小值之差的总和
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
    
        min_prices = prices[0]
        max_prices = prices[0]
        hold_prices = 0
        win_money = 0

        is_up = False

        for i in range(len(prices)-1):

            if (not is_up) and (prices[i] < prices[i+1]):
                hold_prices = prices[i]
                is_up = True

            elif is_up and prices[i] > prices[i+1]:
                win_money += prices[i] - hold_prices
                is_up = False

        if is_up:
            win_money += prices[-1] - hold_prices

        return win_money