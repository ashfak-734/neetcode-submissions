import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:      
        q = deque()
        maxheap = []
        counter = {}

        for i in tasks:
            counter[i] = counter.get(i,0)+1

        for i in counter.values():
            heapq.heappush(maxheap,-1*i)
        
        t = 0
        while maxheap or q:
            t += 1
            
            while q and  q[0][1] == t:
                 count, _ = q.popleft()
                 heapq.heappush(maxheap, count)
                 
            if maxheap:
               count = heapq.heappop(maxheap)
            
               if count+1 < 0:
                  q.append((1+ count,t+n+1))



        return t 


        

        

        