class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        opened = ['(', '[', '{']
        closed = [')', ']', '}']
        stack = []
        for bra in s:
        # idea: stack open brackets until a closed is caught
            if bra in opened:
                stack.append(bra)
            else:
                if stack == []:
                # return false if closed added without open
                    return False
                if opened.index(stack[-1]) == closed.index(bra):
                # if closed appears, compare it with highest element in stack (necessarily open)
                # if matching, pop open bracket from stack
                    stack.pop()
                else:
                # if not matching, return false
                    return False
        if stack:
        # if stack still has open brackets, return false
            return False
        return True