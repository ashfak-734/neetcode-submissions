import heapq

class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None: 
        if len(self.maxheap) < len(self.minheap) +1:      
           heapq.heappush(self.maxheap,-1*num)
           if self.minheap and -1*self.maxheap[0] > self.minheap[0]:
              right = heapq.heappop(self.minheap)
              left =  heapq.heappop(self.maxheap)
              heapq.heappush(self.minheap,-1*left)
              heapq.heappush(self.maxheap,-1*right)
        else:     
           heapq.heappush(self.minheap,num)
           if self.minheap[0] < -1*self.maxheap[0]:
              right = heapq.heappop(self.minheap)
              left =  heapq.heappop(self.maxheap)
              heapq.heappush(self.minheap,-1*left)
              heapq.heappush(self.maxheap,-1*right)

      

    def findMedian(self) -> float:
        lenght = len(self.minheap) + len(self.maxheap)

        if lenght % 2 == 0: #even
            return float((-1*self.maxheap[0] + self.minheap[0])/2)
        else:
            return -1*self.maxheap[0]



           

        
       


        
        