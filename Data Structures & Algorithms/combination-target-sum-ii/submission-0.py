class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res , sol = [], []
        candidates.sort()
        #[1, 2, 2, 4, 5, 6, 9]

        def backtrack(i,total):
            if total == target:
                res.append(sol[:])
                return 

            if total > target or i == len(candidates):
                return 
            
            sol.append(candidates[i])

            backtrack(i+1,total+candidates[i])
            sol.pop()
            
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            backtrack(i+1,total)

        backtrack(0,0)  
        
        return res 
