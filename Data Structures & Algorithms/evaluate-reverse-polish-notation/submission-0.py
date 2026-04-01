class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for token in tokens: 
            if token.isdigit():
                stack.append(token)
            elif token.startswith('-') and len(token) > 1:
                stack.append(token)
            elif len(stack) >= 2 and len(token) == 1 and token in "+/*-":
                b = int(stack.pop())
                a = int(stack.pop())
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == '/':
                    stack.append(int(a / b))
        return int(stack[0])
                      