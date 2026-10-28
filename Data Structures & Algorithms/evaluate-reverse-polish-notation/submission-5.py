class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {'+', '-', '*', '/'}
        stack = []
        
        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b
        }
        
        for i in range(len(tokens)):
            if tokens[i] not in operations:
                stack += [int(tokens[i])]
            else:
                y = int(stack.pop())
                x = int(stack.pop())
                stack += [ops[tokens[i]](x, y)]

        return int(stack[len(stack) - 1])