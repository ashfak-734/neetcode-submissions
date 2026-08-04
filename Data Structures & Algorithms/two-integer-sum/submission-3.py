class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i,v in enumerate(nums):
            difference = target - v
            if difference in seen:
                return [seen[difference], i]
            seen[v] = i



        

    



        



        