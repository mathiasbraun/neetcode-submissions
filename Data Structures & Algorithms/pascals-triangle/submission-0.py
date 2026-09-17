class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]
        for i in range(1, numRows):
            pascal.append([1])
            for j in range(1, i):
                pascal[i].append(pascal[i-1][j-1] + pascal[i-1][j])
            pascal[i].append(1)
        return pascal
