from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g = defaultdict(list)

        for a,b in edges:
            g[a].append(b)
            g[b].append(a)

        seen = set()      
        
        def dfs(i,prev):
            if i in seen:
                return False 
            
            seen.add(i)

            for nei in g[i]:
                if nei == prev:
                    continue

                if not dfs(nei,i):
                    return False 

            return True 

        return dfs(0,-1) and n == len(seen)


        