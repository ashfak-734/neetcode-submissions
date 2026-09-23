class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        number =  {"2":"abc",
                    "3":"def",
                    "4":"ghi",
                      "5":"jkl",
                      "6":"mno",
                      "7":"pqrs",
                      "8":"tuv",
                      "9":"wxyz"}
        res = []
        ans = []

        if digits == "":
            return []

        def backtrack(i):
            if i == len(digits):
                res.append("".join(ans))
                return 

            for c in number[digits[i]]:
                ans.append(c)
                backtrack(i+1)
                ans.pop()
        

        
        backtrack(0)
        return res 

            

        