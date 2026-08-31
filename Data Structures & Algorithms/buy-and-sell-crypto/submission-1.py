class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        profit = 0
        minimum = prices[0]

        for i in range(len(prices)):
            if prices[i] - minimum > profit:
                profit = prices[i] - minimum
            if prices[i] < minimum:
                minimum = prices[i]

        return profit