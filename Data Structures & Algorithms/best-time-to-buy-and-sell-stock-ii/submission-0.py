class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            profit_from_yesterday = prices[i] - prices[i - 1]

            if profit_from_yesterday > 0:
                profit = profit + profit_from_yesterday

        return profit
