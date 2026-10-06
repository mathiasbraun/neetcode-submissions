class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        if m < n:
            return False

        if m == 1:
            if n == 0:
                return True
            else:
                return flowerbed[0] == 0

        for i in range(m):
            # edge cases
            if flowerbed[i] == 1:
                continue
            elif i == 0:
                if flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            elif i == m - 1:
                if flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            elif (flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
            if n == 0:
                return True

        return False