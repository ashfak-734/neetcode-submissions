class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            s = set()
            for j in range(9):
               if board[i][j] == ".":
                 continue
               if board[i][j] not in s:
                  s.add(board[i][j])
               else:
                  return False


        for i in range(9):
            s = set()
            for j in range(9):
               if board[j][i] == ".":
                 continue
               if board[j][i] not in s:
                  s.add(board[j][i])
               else:
                  return False

        starting_point = [(0,0),(0,3),(0,6),
                          (3,0),(3,3),(3,6),
                          (6,0),(6,3),(6,6)]

        for i,j in starting_point:
            s = set()
            for row in range(i,i+3):
                for col in range(j,j+3):
                    if board[row][col] == ".":
                       continue
                    if board[row][col] not in s:
                       s.add(board[row][col])
                    else:
                       return False

        return True 
                   


        
        
            
             

    
     

        