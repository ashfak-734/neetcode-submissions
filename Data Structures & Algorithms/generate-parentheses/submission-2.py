class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open = 0
        close = 0
        
        res, sol  = [], []
        def backtrack(i):
            nonlocal open
            nonlocal close

            if len(sol) == n*2:
                res.append("".join(sol))

            if open<n:
                sol.append("(")
                open+=1
                backtrack(i+1)
                sol.pop()
                open -= 1

            if open > close:
                sol.append(")")
                close += 1
                backtrack(i+1)
                sol.pop()
                close -= 1

        backtrack(0)

        return res 
        