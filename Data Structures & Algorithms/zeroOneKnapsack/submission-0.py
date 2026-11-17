class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        cache = [[-1] * (capacity + 1) for _ in range(len(profit))]
        return self.dfs(0, capacity, profit, weight, cache)

    def dfs(self, i, capacity, profit, weight, cache):
        if i == len(profit):
            return 0
        if cache[i][capacity] != -1:
            return cache[i][capacity]

        # Skip item i
        maxprofit = self.dfs(i + 1, capacity, profit, weight, cache)

        # Include item i
        newcapacity = capacity - weight[i]
        if newcapacity >= 0:
            p = profit[i] + self.dfs(i + 1, newcapacity, profit, weight, cache)
            maxprofit = max(maxprofit, p)
        
        cache[i][capacity] = maxprofit
        return maxprofit