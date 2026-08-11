class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        opened = ['(', '[', '{']
        closed = [')', ']', '}']
        stack = []
        for bra in s:
            if bra in opened:
                stack.append(bra)
            else:
                if stack == []:
                    return False
                if opened.index(stack[-1]) == closed.index(bra):
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True