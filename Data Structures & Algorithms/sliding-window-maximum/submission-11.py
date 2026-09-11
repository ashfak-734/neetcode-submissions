from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        l = 0
        for r in range(k):
            while q and  nums[r] > nums[q[-1]]:
                q.pop()

            q.append(r)
        
            if r+1 >= k:
               res.append(nums[q[0]])   # R[1,-1]  q[1,-1]
               l += 1
        #[1,-1]     
        #    |       
        #      |
        for r in range(k,len(nums)):
            while q and  nums[r] > nums[q[-1]]:
                  q.pop()

            q.append(r)

            while q and q[0] < l :
                q.popleft()

            res.append(nums[q[0]])
            l += 1

        return res


                