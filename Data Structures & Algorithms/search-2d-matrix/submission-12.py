class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.searchRow(matrix, target)

        return self.binarySearch(matrix[row], target)


    def searchRow(self, matrix: List[List[int]], target: int) -> int:
        l, h = 0, len(matrix) - 1
        # pointer l for lower, h for higher

        while l < h and h - l > 1:
            m = (l + h) // 2

            if matrix[m][0] > target:
                h = m
            elif matrix[m][0] < target:
                l = m
            else:
                return m

        if l == h:
            return l
        elif matrix[h][0] > target:
            return l
        else:
            return h

    def binarySearch(self, entries: List[int], target: int) -> bool:
        l, r = 0, len(entries) - 1
        # pointer l for left, r for right

        while l <= r:
            m = (l + r) // 2

            if entries[m] > target:
                r = m - 1
            elif entries[m] < target:
                l = m + 1
            else:
                return True

        return False