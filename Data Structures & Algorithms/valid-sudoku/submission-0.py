class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #check dupe in rows
        for i in range(9):
            s = set()
            for j in range(9):
                current_position = board[i][j]
                if current_position in s:
                    return False
                elif current_position != ".":
                    s.add(current_position)

        #check dupe in col 
        for i in range(9):  #0  
            s = set()
            for j in range(9):   #1
                current_position = board[j][i]   # j = 1 i = 0
                if current_position in s:
                    return False
                elif current_position != ".":
                    s.add(current_position)




        #check dupe in box
        starts = [(0,0),(0,3),(0,6),
                  (3,0),(3,3),(3,6),
                  (6,0),(6,3),(6,6)]

        for i,j in starts:
            s = set()
            for row in range(i, i+3):
                 for col in range(j, j+3):
                   current_position = board[row][col]
                   if current_position in s:
                      return False
                   elif current_position != ".":
                      s.add(current_position)

        return True
    
     

        