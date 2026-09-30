class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m1, m2 = {}, {}

        for row in range(len(mat1)):
            for col in range(len(mat1[0])):
                if mat1[row][col] != 0:
                    m1[(row, col)] = mat1[row][col]

        for row in range(len(mat2)):
            for col in range(len(mat2[0])):
                if mat2[row][col] != 0:
                    m2[(row, col)] = mat2[row][col]

        n = len(mat1)
        m = len(mat2[0])
        product = [[0 for j in range(m)] for i in range(n)]

        for i, k in m1:
            for l, j in m2:
                if k == l and m1[(i, k)] != 0 and m2[(l, j)] != 0:
                    product[i][j] += m1[(i, k)] * m2[(l, j)]

        return product