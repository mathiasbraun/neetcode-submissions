class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        count = 0
        for i in range(len(mat)):
            if i != len(mat) - 1 - i:
                count += mat[i][i] + mat[i][len(mat) - 1 - i]
            else:
                count += mat[i][i]
        return count