import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            distance = float(math.sqrt(x**2 + y**2))

            if len(heap) >= k:
                heapq.heappushpop(heap,(-1*distance,x,y))
            else:
                heapq.heappush(heap,(-1*distance,x,y))
        
        res = []

        while heap:
            _,x,y = heapq.heappop(heap)
            res.append([x,y])

        return res



        