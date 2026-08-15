class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       n = len(matrix[0])
       l,r = 0,(len(matrix)*n)-1

       while l<=r:
          m = (l+r)//2
          i = m//n
          j = m%n
          M = matrix[i][j]

          if M == target:
             return True 
          elif M > target:
              r = m-1
          else:
              l = m+1

       return False

       

            
                

        