class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = [0]*len(nums)
        right = [0]*len(nums)

        l_multi = 1
        r_multi = 1

        for i in range(len(nums)):
            j = -1-i

            left[i] = l_multi
            right[j] = r_multi

            l_multi *= nums[i]
            r_multi *= nums[j]

        result = []
        for x,y in zip(left,right):
            result.append(x*y)

        return result 



        