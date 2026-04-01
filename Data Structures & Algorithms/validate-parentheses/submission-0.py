class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '{':'}', '[':']'}
        stack = list()
        for char in s:
            if char in brackets:
                stack.append(char)
            elif stack and brackets[stack[-1]] == char:
                stack.pop()
            else:
                return False
        return stack == []