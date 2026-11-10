class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        ''' Naive sorting ansatz
        weight.sort()
        number = 0
        total_weight = 0
        for i in range(len(weight)):
            total_weight += weight[i]
            if total_weight > 5000:
                return number
            number += 1

        return len(weight)'''

        # Ansatz by counting sort
        weight_distr = {}
        for w in weight:
            weight_distr[w] = weight_distr.get(w, 0) + 1

        number = 0
        total_weight = 0
        for w in weight_distr.keys():
            while weight_distr[w]:
                total_weight += w
                weight_distr[w] -= 1
                if total_weight > 5000:
                    return number
                number += 1

        return len(weight)