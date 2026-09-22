class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest_price = prices[0]
        best_profit = 0

        for price in prices[1:]:
            best_profit = max(best_profit, price - lowest_price)
            lowest_price = min(lowest_price, price)

        return best_profit
