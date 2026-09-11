class Solution:
    def trap(self, height: List[int]) -> int:
        h = height
        n = len(h)

        leftmax = [0]*n
        rightmax = [0]*n

        l_max = 0
        r_max = 0
        
        j = n-1

        for i in range(n):
            j = -1-i
            leftmax[i] = l_max
            rightmax[j] = r_max

            l_max = max(l_max,h[i])
            r_max = max(r_max,h[j])
        
        result = 0
        for i in range(n):
            trap = min(leftmax[i],rightmax[i]) - h[i]

            if trap > 0:
               result += trap

        return result 


