class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()

        for val in tokens:
            if val in "+-*/":
                if stack:
                    b = int(stack.pop())
                    a = int(stack.pop())
                    if val == "+":
                        stack.append(a + b)
                    elif val == "-":
                        stack.append(a - b)
                    elif val == "*":
                        stack.append(a * b)
                    elif val == "/":
                        stack.append(int(a / b))
            else:
                stack.append(val)
        return int(stack[0])