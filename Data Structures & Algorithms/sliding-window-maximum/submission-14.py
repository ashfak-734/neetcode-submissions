from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        
        #[1,-1]
        #    |
        #    |
        l = 0       # Q[-1]
                    # R[1]

        for r in range(k):   # k = 1  r = 0
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)
    

        res = []
        res.append(nums[q[0]])

        for r in range(k,len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if r-l+1 > k:
                l += 1
            
            if l > q[0]: #1 > 0
                q.popleft()

            res.append(nums[q[0]])

        return res


