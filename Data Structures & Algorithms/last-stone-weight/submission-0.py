import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        h = stones
        heapq.heapify(h)

        while len(h)!= 1:
            first = heapq.heappop(h)
            second = heapq.heappop(h)
            
            heapq.heappush(h,first-second)

        return -(h[0])

        
        