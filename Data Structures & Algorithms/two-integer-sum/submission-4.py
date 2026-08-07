class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}

        for i,v in enumerate(nums):
            difference = target - v

            if difference not in d:
                d[v] = i
            else:
                 return [d[difference],i]





        

    



        



        