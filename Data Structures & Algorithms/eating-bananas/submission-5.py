import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_tests(k):
            hours = 0
            for i in piles:
                hours += math.ceil(float(i/k))
                
            return hours<=h


        l = 1
        r = max(piles)

        while l<r:
            k = (l+r)//2

            if k_tests(k):
                r = k
            else:
                l = k+1

        return r
                
        
  