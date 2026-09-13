class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(r,c):
            if r<0 or c < 0 or r >= m or c >= n or grid[r][c] != 1:
                return 

            count[0] += 1
            
            grid[r][c] = 0

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

           
  
        max_area = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    count = [0]
                    dfs(r,c)
                    max_area = max(max_area,count[0])

        return max_area
        