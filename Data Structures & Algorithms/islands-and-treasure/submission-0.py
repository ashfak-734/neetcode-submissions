from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        m = len(grid)
        n = len(grid[0])
        

        visit = set()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        
        def addgrid(r,c):
            if r<0 or c < 0 or r >= m or c >= n or (r,c) in visit or grid[r][c] == -1:
                return 

            q.append((r,c))
            visit.add((r,c))
                      
        dist = 0
        while q:

            for _ in range(len(q)):
               r,c = q.popleft()
               grid[r][c] = dist 
               addgrid(r+1,c)
               addgrid(r-1,c)
               addgrid(r,c+1)
               addgrid(r,c-1)

            dist += 1


        

        