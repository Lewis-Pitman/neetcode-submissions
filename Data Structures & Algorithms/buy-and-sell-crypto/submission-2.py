class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left =  0

        best = 0

        for i in range(1, len(prices)):
            if prices[i] < prices[left]:
                left = i
            else:
                profit = prices[i] - prices[left]
                best = max(best, profit)
        
        return best
