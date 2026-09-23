import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        total_cost = 0
        minheap = [(0,0)]
        seen = set()

        while len(seen) < n:
            dist,i = heapq.heappop(minheap)
            if i in seen:
                continue

            total_cost += dist
            seen.add(i)
            xi,yi = points[i]

            for j in range(n):
                if j not in seen:
                    xj,yj = points[j]
                    dist = abs(xi-xj)+ abs(yi-yj)
                    heapq.heappush(minheap,(dist,j))


        return total_cost
        