import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        visited = {(0,0)}
        minheap = [(grid[0][0],0,0)]


        while minheap:
            t,r,c = heapq.heappop(minheap)

            if r == m-1 and c == n-1:
                return t

            for R,C in directions:
                neiR,neiC = r+R,c+C
                
                if (neiR<0 or neiC<0 or neiR==m or neiC == n or (neiR,neiC) in visited):
                    continue

                heapq.heappush(minheap,(max(t,grid[neiR][neiC]),neiR,neiC))
                visited.add((neiR,neiC))

        