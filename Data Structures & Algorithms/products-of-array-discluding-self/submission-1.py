class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]*n
        postfix = [0]*n
        
        l_multi = 1
        r_multi = 1


        for i in range(n):
            j = -i-1
            prefix[i] = l_multi
            postfix[j] = r_multi
            l_multi *= nums[i]
            r_multi *= nums[j]

        result = [x*y for x,y in zip(prefix,postfix)]

        return result


        

        