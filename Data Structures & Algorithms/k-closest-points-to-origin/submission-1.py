import heapq
import math 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        def distance(x,y):
            return float(math.sqrt(x**2+y**2))

        for x,y in points:
            d = distance(x,y)

            if len(heap)<k:
                heapq.heappush(heap,(-d,x,y))
            else:
                heapq.heappushpop(heap,(-d,x,y))
            
        return [[x,y] for _,x,y in heap]

























        

        

        