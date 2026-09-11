class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      for row in range(9):
         s = set()
         for col in range(9):
            if board[row][col] in s:
               return False
            
            if board[row][col] != ".":
               s.add(board[row][col])

      for row in range(9):
         s = set()
         for col in range(9):
            if board[col][row] in s:
               return False
            
            if board[col][row] != ".":
               s.add(board[col][row])


      start = [(0,0),(0,3),(0,6),
               (3,0),(3,3),(3,6),
               (6,0),(6,3),(6,6)]

      for i in start:
         x,y = i
         s = set()
         for row in range(x,x+3):
            for col in range(y,y+3):
                if board[row][col] in s:
                   return False
            
                if board[row][col] != ".":
                   s.add(board[row][col])


      return True 

               

        