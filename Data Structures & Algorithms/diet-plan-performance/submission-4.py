class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        score = 0
        T = sum(calories[:k])
        for i in range(k, len(calories)):
            if T < lower:
                score -= 1
            elif T > upper:
                score += 1
            T += calories[i] - calories[i - k]

        if T < lower:
            return score - 1
        elif T > upper:
            return score + 1
        return score