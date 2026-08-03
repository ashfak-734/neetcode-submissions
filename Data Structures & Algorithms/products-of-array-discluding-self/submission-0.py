class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [0]*len(nums)
        postfix = [0]*len(nums)

        l_multi = 1 # 1 * 1 
        r_multi = 1 # 1 * 4

        for i in range(len(nums)): # 0
            j = -i-1               # -1
            prefix[i] = l_multi       
            postfix[j] =  r_multi
            l_multi *= nums[i]
            r_multi *= nums[j]

        result = [x*y for x,y in zip(prefix,postfix)]
        return result

        

        