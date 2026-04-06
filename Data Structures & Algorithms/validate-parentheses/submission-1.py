class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        map = {"(":")", "{":"}", "[":"]"}
        for char in s:
            if stack and map[stack[-1]] == char:
                stack.pop()
            elif char in map:
                stack.append(char)
            else:
                return False # return false if the stack is empty and char is not in the map
        return stack == []