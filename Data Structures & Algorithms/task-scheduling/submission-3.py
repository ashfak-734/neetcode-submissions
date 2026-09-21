import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = collections.deque()
        
        count = {}
        for task in tasks:
            count[task] = count.get(task,0) + 1
        
        maxheap = []

        for val in count.values():
            heapq.heappush(maxheap, -1*val)
        
        t = 0

        while maxheap or q:
            t += 1
                                       
            while q and q[0][1] == t:
                count,_ = q.popleft()
                if count<0:
                   heapq.heappush(maxheap,count)
            
            if maxheap:
               val = heapq.heappop(maxheap)

               if val < -1:
                  q.append((val+1,t+n+1))

        return t 

             
             


        