class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l<=r:
            m = (l+r)//2

            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        min_r = r

        if min_r == 0:
            l,r = 0,len(nums)-1

        if target >= nums[0] and target<=nums[min_r-1]:
            l,r = 0,min_r-1
        
        if target>=nums[min_r] and target<=nums[len(nums)-1]:
            l,r = min_r, len(nums)-1



        while l<=r:
            m = (l+r)//2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            else:
                r = m-1

        return -1

        