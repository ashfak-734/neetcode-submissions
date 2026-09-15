from collections import deque 
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        A_q = deque()
        P_q = deque()

        m = len(heights)
        n = len(heights[0])
        
        seen_p = set()
        seen_a = set()
    

        # Pacific Ocean — top row
        for j in range(n):
            P_q.append((0, j))
            seen_p.add((0, j))

        # Pacific Ocean — left column
        for i in range(m):
            P_q.append((i, 0))
            seen_p.add((i, 0))

        # Atlantic Ocean — right column
        for i in range(m):
            A_q.append((i, n - 1))
            seen_a.add((i, n - 1))

        # Atlantic Ocean — bottom row
        for j in range(n):
            A_q.append((m - 1, j))
            seen_a.add((m - 1, j))
            

    
        def get_cords(q,seen):
            while q:
                i,j = q.popleft()
                
                for r,c in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0 <= r < m and 0 <= c < n and (r,c) not in seen and heights[r][c] >= heights[i][j]:
                        q.append((r,c))
                        seen.add((r,c))

            
        get_cords(P_q,seen_p)
        get_cords(A_q,seen_a)

        return list(seen_p.intersection(seen_a))






                



            

                






        

        




        