class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        if n == 0: return ""
        res = []
        # 1. base case if open_count == closed_count == n: parenthesis are generated, add to res
        # 2. start with open brackets only open_count < n then backtrack
        # 3. add close bracket when close_count < open_count then backtrack
        def backtrack(open_count, closed_count, build_par):
            if open_count == closed_count == n:
                res.append("".join(build_par))
                return

            if open_count < n:
                build_par.append("(")
                backtrack(open_count + 1, closed_count, build_par)
                build_par.pop()
            
            if closed_count < open_count:
                build_par.append(")")
                backtrack(open_count, closed_count+ 1, build_par)
                build_par.pop()
        
        backtrack(0, 0, [])
        return res