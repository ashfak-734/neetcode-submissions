import heapq
import math 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []

        for i in points:
            x,y = i
            distance = float(math.sqrt(x**2+y**2))
            heapq.heappush(heap,(distance,i))

        while len(result) != k:
            result.append(heapq.heappop(heap)[1])

        return result 

        

        