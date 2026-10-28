class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Go through diagonal, check horizontally and vertically
        for i in range(9):
            seen_hor = set()
            seen_ver = set()
            for k in range(9):
                if (board[i][k] in seen_hor 
                    or board[k][i] in seen_ver):
                    return False
                if board[i][k] != '.':
                    seen_hor.add(board[i][k])
                if board[k][i] != '.':
                    seen_ver.add(board[k][i])

        # Go through each subsquare of area 9
        for i in range(3):
            for j in range(3):
                seen = set()
                for k in range(3):
                    for l in range(3):
                        if board[3 * i + k][3 * j + l] in seen:
                            return False
                        elif board[3 * i + k][3 * j + l] != '.':
                            seen.add(board[3 * i + k][3 * j + l])

        return True