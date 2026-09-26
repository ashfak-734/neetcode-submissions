class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        def backtrack(r,c,i):
            if i == len(word):
                return True 

            if r<0 or c<0 or r==m or c==n or word[i] != board[r][c]:
                return False 
            
            temp = board[r][c]
            board[r][c] = "#"     

            if (backtrack(r+1,c,i+1) or 
            backtrack(r-1,c,i+1)  or
            backtrack(r,c+1,i+1)  or
            backtrack(r,c-1,i+1)):
               return True 

            board[r][c] = temp
            
            


        for r in range(m):
            for c in range(n):
                if backtrack(r,c,0):
                    return True 

        return False 

        