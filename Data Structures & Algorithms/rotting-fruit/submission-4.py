from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten,fresh,empty = 2,1,0
        num_fresh = 0
        m = len(grid)
        n = len(grid[0])
        q = deque()
        visit = set()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == rotten:
                    q.append((r,c))
                elif grid[r][c] == fresh:
                    num_fresh += 1

        if num_fresh == 0:
            return 0

        num_minutes = -1
        
        def addgrid(r,c):
            nonlocal num_fresh 
            if 0 <= r < m and 0 <= c < n and grid[r][c] == fresh:     
                grid[r][c] = rotten
                num_fresh -= 1
                q.append((r,c))

        while q:
            q_size = len(q)
            num_minutes += 1

            for _ in range(q_size):
                r,c = q.popleft()
                addgrid(r+1,c)
                addgrid(r-1,c)
                addgrid(r,c+1)
                addgrid(r,c-1)


        if num_fresh == 0:
            return num_minutes
        else:
            return -1

 


                
            

        