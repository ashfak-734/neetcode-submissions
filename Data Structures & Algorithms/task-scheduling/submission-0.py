import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {}
        q = deque()

        for i in tasks:
            counter[i] = counter.get(i,0) + 1

        # [2,2]
        heap = [-i for i in counter.values()]
        heapq.heapify(heap)
        
        t = 0

        while heap or q:
            t += 1

            if heap:
               cnt = 1+ heapq.heappop(heap)
               if cnt:
                  q.append([cnt,t+n])


            if q and q[0][1] == t:
                heapq.heappush(heap,q.popleft()[0])
                

        return t


        


            

        