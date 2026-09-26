class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res,sol = [],[]

        def isPali(s,i,j):
            substring = s[i:j+1]
            l = 0
            r = len(substring) -1
            while l<=r:
                if substring[l] != substring[r]:
                    return False  
                l += 1
                r -= 1

            return True 

        def backtrack(i):
            if i == len(s):
                res.append(sol[:])

            for j in range(i,len(s)):
                if isPali(s,i,j):
                    sol.append(s[i:j+1])
                    backtrack(j+1)
                    sol.pop()

        backtrack(0)
        return res 





        