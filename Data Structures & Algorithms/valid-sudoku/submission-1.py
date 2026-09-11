class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        for i in range(9):
            s = set()
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if val not in s:
                    s.add(val)
                else:
                    return False


        for i in range(9):
            s = set()
            for j in range(9):
                val = board[j][i]
                if val == ".":
                    continue
                if val not in s:
                    s.add(val)
                else:
                    return False

        
        starting_point = [(0,0),(0,3),(0,6),
                          (3,0),(3,3),(3,6),
                          (6,0),(6,3),(6,6)]

        for i,j in starting_point:
            s = set()
            for row in range(3):
                for col in range(3):
                    val = board[i+row][j+col]
                    if val == ".":
                       continue
                    if val not in s:
                        s.add(val)
                    else:
                        return False


        return True

        
            
             

    
     

        