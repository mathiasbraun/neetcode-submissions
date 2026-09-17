class Solution:
    def countElements(self, arr: List[int]) -> int:
        seen = set(arr)
        count = 0

        for n in arr:
            if n + 1 in seen:
                count += 1
        return count