class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #[-3, -3, -2, -1, 0, 1, 2, 2, 3]
        
        result = []
        for i in range(len(nums)):

            if nums[i] > 0:
                break

            if i>0 and nums[i] == nums[i-1]:
                continue

            lo = i+1
            hi = len(nums) -1 

            while lo<hi:
                current_sum = nums[i] + nums[lo] + nums[hi]

                if current_sum == 0:
                    result.append([nums[i],nums[lo],nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo<hi and nums[lo] == nums[lo-1]:
                        lo += 1
                    while lo<hi and nums[hi] == nums[hi+1]:
                        hi -= 1
                elif current_sum < 0:
                    lo += 1
                else:
                    hi -= 1

             
        return result

        

                    






        