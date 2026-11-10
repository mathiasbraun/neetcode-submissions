class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        number = 0
        total_weight = 0
        for i in range(len(weight)):
            total_weight += weight[i]
            if total_weight > 5000:
                return number
            number += 1
        
        return len(weight)