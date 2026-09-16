from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses  = prerequisites           
        result = []
        g = defaultdict(list)
        
        UNVISITED = 0
        VISITED = 2
        VISITING = 1 

        states = [0]*numCourses

        for a,b in courses:
            g[a].append(b)

        def courses(node):
            state = states[node]
            
            if state == VISITING:
                return False
            elif state == VISITED:
                return True 
            
            states[node] = VISITING

            for nei in g[node]:
                if not courses(nei):
                    return False 
            
            states[node] = VISITED
            result.append(node)
            return True 

        for i in range(numCourses):
            if not courses(i):
                return []

        return result 

        





        
        