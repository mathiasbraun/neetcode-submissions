# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs:
            return []

        if len(pairs) == 1:
            return pairs

        pivot_pair = pairs[len(pairs) - 1]
        pivot = pivot_pair.key

        i = 0
        for j in range(len(pairs) - 1):
            if pairs[j].key < pivot:
                pairs[i], pairs[j] = pairs[j], pairs[i]
                i += 1
        
        pairs[i], pairs[len(pairs) - 1] = pairs[len(pairs) - 1], pairs[i]

        left = self.quickSort(pairs[0:i])
        right = self.quickSort(pairs[i+1:len(pairs)])

        return left + [pairs[i]] + right