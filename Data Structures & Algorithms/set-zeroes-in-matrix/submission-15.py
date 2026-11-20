class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ''' Solution with O(m + n) space
        rows, cols = set(), set()
        m, n = len(matrix), len(matrix[0])

        # Collect positions of zeros
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        # Overwrite nonzeros
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0'''

        m, n = len(matrix), len(matrix[0])
        firstRowZero = any(matrix[0][j] == 0 for j in range(n))

        # Idea: when we find 0 in matrix[i][j] then set
        # matrix[i][0] = 0 and matrix[0][j] = 0.
        # Afterwards iterate over first row and column
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(m):
                matrix[i][0] = 0

        if firstRowZero:
            for j in range(n):
                matrix[0][j] = 0